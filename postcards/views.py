# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Postcard


# Create your views here.
@login_required(login_url='/login/')
def all_postcards(request):
    postcards = Postcard.objects.all()
    return render(request, 'postcards/postcards.html', {'postcards': postcards})
