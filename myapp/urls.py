from django.urls import path
from .views import ItemListCreate,ProcessURLView

urlpatterns = [
    # path('items/', ItemListCreate.as_view(), name='item-list-create'),
	path('scrapeIns/', ProcessURLView.as_view(), name='scrapeIns'),
]
