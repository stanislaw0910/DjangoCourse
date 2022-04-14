from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=20, required=False)
    last_name= forms.CharField(max_length=20, required=False)
    email = forms.EmailField(required=True)
    city=forms.CharField(max_length=30, required=False)
    date_of_birth=forms.DateField(required=False)
    phone_number=forms.IntegerField(required=False)
    card_number=forms.IntegerField(required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class RestorePasswordForm(forms.Form):
    email = forms.EmailField()