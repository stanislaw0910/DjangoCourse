from django.http import HttpResponseRedirect
from .forms import UserForm
from django.views import View
from django.shortcuts import render
from .models import User


class UserFormView(View):

    def get(self, request):
        user_form = UserForm()
        return render(request, 'profiles/register.html', context={'user_form': user_form})

    def post(self, request):
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            User.objects.create(**user_form.cleaned_data)
            return HttpResponseRedirect('/')
        return render(request, 'profiles/register.html', context={'user_form': user_form})
