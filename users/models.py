from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=30, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    card_number = models.IntegerField(null=True, blank=True)