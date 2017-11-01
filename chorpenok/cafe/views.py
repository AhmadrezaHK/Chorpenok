# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import DetailView
from .models import Cafe

# Create your views here.

class CafeListView(ListView):
    model = Cafe
    template_name = "firstpage.html"

class CafeDetailView(DetailView):
    template_name = 'cafe-detail.html'