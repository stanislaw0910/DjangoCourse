from django.contrib import admin
from django.urls import path, include
from profiles.views import UserFormView
from .views import MainView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='Main'),
    path('profiles/register', UserFormView.as_view()),
    path('news/', include('news.urls')),
    path('users/', include('users.urls')),
    path('media/', include('media.urls')),
    path('goods/', include('goods.urls'))

]

