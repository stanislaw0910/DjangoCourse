from django.urls import path
from .views import item_list, upload_prices


urlpatterns = [
    path('items', item_list, name='items'),
    path('upload', upload_prices, name='upload-prices')
]