from django.urls import path
from . import views


urlpatterns = [
    path('', views.Main_Page.as_view(), name='main_page'),
    path('advertisements', views.AdvertisementListView.as_view(), name='advertisements'),
    path('advertisements/<int:pk>', views.AdvertisementDetailView.as_view(), name='advertisement_detail'),
    path('about', views.About.as_view(), name='about'),

    #path('categories', views.Categories.as_view(), name='categories'),
    #path('contacts', views.Contacts.as_view(), name='contacts'),
    #path('regions', views.Regions.as_view(), name='regions'),
    #path('random', views.RandomAdvert.as_view(), name='random_advert')

]
