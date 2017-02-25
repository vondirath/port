from django.contrib.syndication.views import Feed
from django.urls import reverse


class LatestEntriesFeed(Feed):
    title = "news"
    link = "/link/"
    description = "news feed"

    def items(self):
        return Comment.objects.all().order_by("-pubDate")[:5]

    def item_title(self, item):
          return item.user_name

    def item_description(self, item):
       return item.comment

    def item_link(self, item):
         return reverse('category', kwargs={'object_pk': item.pk})
