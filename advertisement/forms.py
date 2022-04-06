from django import forms


class AdvertisementForm(forms.Form):
    title = forms.CharField(min_length=3, max_length=20)
    description = forms.CharField(min_length=10, max_length=200)
    price = forms.FloatField(min_value=10, max_value=100000)
