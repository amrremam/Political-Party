from django.shortcuts import render
from guest.models import Author, Post
from django.db import connection
from django.db.models import Q


# def guest_list(request):
#     guests = Guest.objects.all()
#     print(guests)
    # print(connection.queries)
    # return render(request, 'index.html', {'guest': guests})


# def guest_all(request):
#     guests = Guest.objects.filter(Q(Lname__startswith='awel') | Q(Lname__startswith='Ftalet') | ~Q
#     (Lname__startswith='samiir'))
#     print(guests)
    # print(connection.queries)
    # return render(request, 'index.html', {'guest': guests})


# def guest_all(request):
    # guests = Guest.objects.all()
    # guests = Guest.objects.all().values_list("lName").union(Admin.objects.all().values_list("lName"))
    # guests = Guest.objects.exclude(fName="amr") & Guest.objects.exclude(age=25)
    # print(guests)
    # print(connection.queries)
    # return render(request, 'index.html', {'guest': guests})



def guest_all(request):
    # guests = Post.objects.all()
    guests = Post.objects.select_related('author').all()
    # guests = Post.objects.select_related('author').filter(author__fName__startswith='messi')
    data = [n.author.fName for n in guests]

    print(guests)
    return render(request, 'index.html', {'guests': data})
