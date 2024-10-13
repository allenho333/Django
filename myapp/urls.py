from django.urls import path
from .views import ItemListCreate,ScrapeIns,ScrapeTiktok
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('items/', ItemListCreate.as_view(), name='item-list-create'),
	path('scrapeIns/', ScrapeIns.as_view(), name='scrapeIns'),
	path('scrapeTiktok/', ScrapeTiktok.as_view(), name='scrapeTiktok'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
