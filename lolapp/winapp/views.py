from django.shortcuts import render
from .summoner_name_form import 
# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World")
