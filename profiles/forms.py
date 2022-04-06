from django import forms
import datetime
from django.core.exceptions import ValidationError


class UserForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()
    first_name=forms.CharField()
    second_name=forms.CharField()
    last_name=forms.CharField()
    email=forms.EmailField()
    birthday=forms.DateField()

    def clean_birthday(self):
        date = self.cleaned_data['birthday']
        today = datetime.date.today()
        year_delta = (today - date).days / 365
        if year_delta < 18:
            raise ValidationError('Your age is under 18')
