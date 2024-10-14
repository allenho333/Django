from django.urls import path
from .views import ItemListCreate,ScrapeIns,ScrapeTiktok


urlpatterns = [ 
    # path('items/', ItemListCreate.as_view(), name='item-list-create'),
	path('scrapeIns/', ScrapeIns.as_view(), name='scrapeIns'),
	path('scrapeTiktok/', ScrapeTiktok.as_view(), name='scrapeTiktok'),
]