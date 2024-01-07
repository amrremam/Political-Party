from django.shortcuts import render, get_object_or_404, redirect
from .models import Member



def add_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        lname = request.POST.get('lname')
        age = request.POST.get('age')

        new_member = Member.objects.create(name=name, lname=lname, age=age)
        
        return render(request, 'dashboard.html', {'user': new_member})
    
    return render(request, 'dashboard.html')


def edit_user(request, user_id):
    user = get_object_or_404(Member, pk=user_id)
    
    if request.method == 'POST':
        user.name = request.POST.get('name')
        user.lname = request.POST.get('lname')
        user.age = request.POST.get('age')
        user.save()

        return render(request, 'test.html', {'user': user})

    return render(request, 'test.html', {'user': user})



def delete_user(request, user_id):
    user = get_object_or_404(Member, pk=user_id)
    
    if request.method == 'POST':
        user.delete()
        return redirect('dashboard.html')

    return render(request, 'dashboard.html', {'user': user})
