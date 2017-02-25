from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.contrib.syndication.views import Feed
from django.urls import reverse
import feedparser
from django.template import Context, Template



# Create your views here.
def index(request):
    feeds = feedparser.parse('http://feeds.abcnews.com/abcnews/topstories')
    
    context = {"feeds" : feeds.entries}

    return render(request, 'rssread/index.html', context)
