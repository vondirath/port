from django.conf.urls import url
from rssread.feeds import LatestEntriesFeed
from . import views

app_name = 'rssread'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^latest/feed/$', LatestEntriesFeed()),
]
