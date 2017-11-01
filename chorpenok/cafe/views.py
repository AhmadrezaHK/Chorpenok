# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Cafe

# Create your views here.

class CafeListView(ListView):
    model = Cafe
    template_name = "firstpage.html"