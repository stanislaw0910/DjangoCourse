from django import forms
from .models import Comments, News
from django.forms import TextInput


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'
        widgets={
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title of news'
            }),
            "description": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'News content'
            }),}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['news', 'user']
        widgets={
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }),
            "text": TextInput(attrs={
                'class': 'form-control',

                'placeholder': 'Comment'
            }), }
