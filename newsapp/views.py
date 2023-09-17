from django.shortcuts import render
from newsapi import NewsApiClient

# Create your views here.

def Index(request):
    newsapi = NewsApiClient(api_key="c85c9ead39f84dce811c8777daba7b1b")
    topHeadlines = newsapi.get_top_headlines(sources='the-times-of-india')

    articles = topHeadlines['articles']
    
    desc = []
    news = []
    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])


    mylist = zip(news, desc, img)
    return render(request, 'index.html', context={"mylist":mylist})

def bbc(request):
    newsapi = NewsApiClient(api_key="c85c9ead39f84dce811c8777daba7b1b")
    topheadlines = newsapi.get_top_headlines(sources='bbc-news')


    articles = topheadlines['articles']

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])


    mylist = zip(news, desc, img)
    return render(request, 'bbc.html', context={"mylist":mylist})