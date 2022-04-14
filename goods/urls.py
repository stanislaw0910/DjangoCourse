from django.urls import path
from .views import item_list, upload_prices, ItemDetail


urlpatterns = [
    path('items', item_list, name='items'),
    path('upload', upload_prices, name='upload-prices'),
    path('items/<int:pk>', ItemDetail.as_view(), name='item-detail')
]