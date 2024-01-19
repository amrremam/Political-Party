from . models import District
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required


# - Login
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('rememberMe') == 'on'

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if not remember_me:
                request.session.set_expiry(0)
            return redirect('app:dashboard')
        else:
            pass

    return render(request, 'user/sign-in.html')


# - Dashboard
@login_required(login_url='login/')
def index(request):
    return render(request, 'user/dashboard.html')


# - Roles
@login_required(login_url='login/')
def roles(request):
    return render(request, 'user/roles.html')


# - Tables
@login_required(login_url='login/')
def tables(request):
    return render(request, 'user/tables.html')
