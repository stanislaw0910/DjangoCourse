from django.urls import path
from .views import upload_file, check_file

urlpatterns = [
    path('upload/', upload_file, name='upload'),
    path('check/', check_file, name='check')
]