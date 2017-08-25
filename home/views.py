# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render


# Create your views here.
# View for Index Page
def get_index(request):
    return render(request, 'index.html')


# View for About Page
def get_about(request):
    return render(request, 'about.html')


# View for Contact Page
def get_contact(request):
    return render(request, 'contact.html')


# View for Gallery Page
def get_gallery(request):
    return render(request, 'gallery.html')


# View for Mandela Page
def get_madiba(request):
    return render(request, 'nelson-mandela.html')


# View for Giraffe Page
def get_giraffe(request):
    return render(request, 'giraffe-and-calf.html')


# View for Elephant Page
def get_elephant(request):
    return render(request, 'vallim-elephant.html')


# View for Terms of Service
def get_terms_of_service(request):
    return render(request, 'privacy-policy.html')
