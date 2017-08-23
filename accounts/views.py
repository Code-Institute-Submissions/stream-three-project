# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from accounts.forms import UserRegistrationForm, UserLoginForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            user = auth.authenticate(email=request.POST.get('email'),
                                     password=request.POST.get('password1'))

            if user:
                messages.success(request, "Welcome, you have successfully registered.")
                return redirect(reverse('profile'))

            else:
                messages.error(request, "Sorry, you are unable to log in at this time.")

    else:
        form = UserRegistrationForm()

    args = {'form': form}
    args.update(csrf(request))

    return render(request, 'register.html', args)


def profile(request):
    return render(request, 'profile.html')


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(email=request.POST.get('email'),
                                     password=request.POST.get('password'))

            if user is not None:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in!")
                return redirect(reverse('profile'))
            else:
                form.add_error(None, "Your email or password was incorrect.")

    else:
        form = UserLoginForm()

    args = {'form': form}
    args.update(csrf(request))
    return render(request, 'login.html', args)


def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out. Hope to see you again soon!')
    return redirect(reverse('index'))
