from django.shortcuts import render
from . models import District



def index(request):
    return render(request, 'user/dashboard.html')


def roles(request):
    return render(request, 'user/leo.html')


def tables(request):
    return render(request, 'user/tables.html')


def signin(request):
    return render(request, 'user/sign-in.html')
