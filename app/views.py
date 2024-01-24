from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required

from django.contrib import messages

from . forms import createUserForm


# - Login
def login_view(request):
    if request.user.is_authenticated:
        return redirect('app:dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('app:dashboard')
            else:
                messages.info(request, 'Invalid Username or Password')

        return render(request, 'user/sign-in.html')


# - Logout
def logout_view(request):
    logout(request)
    return redirect('app:login')


# - Add_new_user
@login_required(login_url='login/')
def new_user(request):
    form = createUserForm()

    if request.method == 'POST':
        form = createUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, ' تم اضافة المستخدم' + user)
            # return redirect('app:dashboard')

    return render(request, 'user/NewUser.html', {'form': form})


# - Dashboard
@login_required(login_url='app:login')
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


# - Permissions
@login_required(login_url='login/')
def permission(request):
    return render(request, 'user/Ozanat.html')


@login_required(login_url='login/')
def addDor(request):
    return render(request, 'user/addDor.html')


@login_required(login_url='login/')
def table(request):
    return render(request, 'user/Table.html')
