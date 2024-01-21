from django.shortcuts import render
from guest.models import Guest
from django.db import connection
from django.db.models import Q


def guest_list(request):
    guests = Guest.objects.all()
    print(guests)
    print(connection.queries)
    return render(request, 'index.html', {'guest': guests})


def guest_detail(request):
    guests = Guest.objects.filter(Q(Lname__startswith='awel') | Q(Lname__startswith='Ftalet') | ~Q
    (Lname__startswith='samiir'))
    print(guests)
    print(connection.queries)
    return render(request, 'index.html', {'guest': guests})
