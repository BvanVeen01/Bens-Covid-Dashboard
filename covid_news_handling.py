# Covid News

def news_API_request(base_url,api_key,api_country,covid_terms= "Covid COVID-19 coronavirus"):
    import requests
    import json

    # Accessing all the news articles
    base_url = base_url
    api_key = api_key
    country = api_country
    complete_url = base_url + "country=" + country + "&apiKey=" + api_key
    response = requests.get(complete_url)
    data = response.json()
    
    # Splitting the covid terms into a list of words
    covid_words = covid_terms.split()
    
    # a list for relevant articles to be added to
    covid_articles=[]
    
    # adds covid related articles to covd_articles
    for i in data['articles']:
        for ii in covid_words:
            if ii in i['title']:
                covid_articles.append(i)
                break
    return covid_articles

def update_news():
    # sets the previous call of news_API_request() to a dataset called old news
    oldnews=news 
    # sets newnews toan up-to-date list of news articles
    newnews=news_API_request(base_url=config["api_base_url"],
                              api_country=config["api_country"],
                              covid_terms=config["terms"],
                              api_key=config["api_key"])
    # removes all articles in newnews that where present in old news
    for i in newnews:
        if i in oldnews:
            newnews.remove(i)
    # replaces all the old values in news with those in newnews
    del news[0:len(news)]
    for ii in newnews:
        news.append(ii)