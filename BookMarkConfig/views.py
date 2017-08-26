from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template.loader import get_template
from django.views.generic import ListView, DetailView
from requests import request

from BookMarkConfig.models import BookMark


class BookmarkLV(ListView):
    model = BookMark


class BookmarkDV(DetailView):
    model = BookMark