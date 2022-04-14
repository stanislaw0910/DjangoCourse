from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import AuthForm, RegisterForm, RestorePasswordForm
from datetime import datetime
from django.contrib.auth import logout
from .models import Profile


def login_view(request):
    if request.method == 'POST':
        auth_form = AuthForm(request.POST)
        if auth_form.is_valid():
            username = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            current_time = int(datetime.now().strftime("%H"))
            if user:
                if current_time>22 or current_time<7:
                    return HttpResponse("You can't login between 22 and 7 hours")
                elif user.is_active:
                    login(request, user)
                    return HttpResponse('Successfully logged in')
                else:
                    auth_form.add_error('__all__', 'ERROR! Account is inactive!')
            else:
                auth_form.add_error('__all__', 'Login or password is wrong')
    else:
        auth_form = AuthForm()
        context = {'form': auth_form}
        return render(request, 'users/login.html', context=context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def register(request):
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            city =form.cleaned_data.get('city')
            date_of_birth=form.cleaned_data.get('date_of_birth')
            phone_number=form.cleaned_data.get('phone_number')
            card_number=form.cleaned_data.get('card_number')
            Profile.objects.create(
                user=user,
                city=city,
                date_of_birth=date_of_birth,
                phone_number=phone_number,
                card_number=card_number
            )
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})


def account(request):
    return render(request, 'users/account.html')


def restore_password(request):
    if request.method== 'POST':
        form = RestorePasswordForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            new_password = User.objects.make_random_password()
            current_user = User.objects.filter(email=user_email).first()
            if current_user:
                current_user.set_password(new_password)
                current_user.save()
            send_mail(
                subject='Restore password',
                message='Test',
                from_email='admin@company.com',
                recipient_list=['any@company.com']
            )
            return HttpResponse('Email with new password was sent successfully')
    restore_password_form = RestorePasswordForm()
    context = {
        'form': restore_password_form
    }
    return render(request, 'users/restore_password.html', context=context)
