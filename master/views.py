from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login

# Create your views here.

def index(request):
    return HttpResponse('hiiiii')

def login_view(request):
    pass

