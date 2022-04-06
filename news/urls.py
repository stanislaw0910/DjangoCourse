from django.contrib import admin
from django.urls import path, include
from .views import NewsCreateView, IndexNews, NewsDetailView, NewsUpdateView


urlpatterns = [
    path('',  IndexNews.as_view()),
    path('create', NewsCreateView.as_view()),
    path('<int:pk>', NewsDetailView.as_view()),
    path('<int:pk>/update', NewsUpdateView.as_view(), name='news-update'),
]