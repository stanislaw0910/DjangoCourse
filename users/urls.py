from django.urls import path
from .views import logout_view, register, account, restore_password
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
    path('account/', account, name='account'),
    path('restore_password/', restore_password, name='restore_password')
]
