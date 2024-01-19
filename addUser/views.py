from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Member


class AddUser(View):
    template_name = 'users/add_user.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        country = request.POST.get('country')
        phone = request.POST.get('phone')

        user = Member(name=name, country=country, phone=phone)
        user.save()

        return redirect('app:dashboard')


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
