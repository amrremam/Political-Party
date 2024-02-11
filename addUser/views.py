from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MemberForm
from app.decorators import allowed_users, unauthenticated_user
from django.db.models import Q


from .models import Member




# - Create
class AddUser(View):
    template_name = 'users/add_user.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        fields = [
            'amana', 'partyde', 'amanaQism', 'amanaSheyakha', 'amanaCairo', 'amanaKetaa', 'Taam',
            'specificLagna', 'pastParty', 'manasebAamma', 'sanaDawra', 'odwyaSabka', 'name',
            'userImg', 'presidentPartyName', 'noaaelAdwiaa', 'famousName', 'NationalId', 'NationalIdImg',
            'age', 'yearBirth', 'monthBirth', 'dayBirth', 'education', 'workProfession', 'nekaba',
            'ketaaAamel', 'currentlyWorkProfession', 'martialStatus', 'mobileOne', 'mobileTwo', 'landline',
            'email', 'rakmElmabna', 'street', 'district', 'city', 'qism', 'ketaa', 'mohafza',
        ]

        data = {field: request.POST.get(field) for field in fields}

        user = Member(**data)
        user.save()

        return redirect('addUser:show_user')



# - Read
@login_required(login_url='app:login')
def show_user(request, *args, **kwargs):

    # - Search Query
    if 'q' in request.GET:
        q = request.GET['q']
        # data = Member.objects.filter(name__icontains=q)
        kaza_q = Q(Q(name__icontains=q)) | Q(Q(email__icontains=q))
        data = Member.objects.filter(kaza_q)
    else:
        data = Member.objects.all()

    context = {
        'data': data
    }
    return render(request, 'user/Table.html', context)




# - Update
@login_required(login_url='app:login')
@allowed_users(allowed_roles=['admin'])
def update_user(request, user_id):
    user = get_object_or_404(Member, pk=user_id)

    if request.method == 'POST':
        form = MemberForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('app:dashboard')
    else:
        form = MemberForm(instance=user)

    return render(request, 'user/update_user.html', {'form': form, 'user': user})



# - Delete
@login_required(login_url='app:login')
@allowed_users(allowed_roles=['admin'])
def delete_user(request, user_id):

    try:
        user = get_object_or_404(Member, pk=user_id)

        user.delete()

        messages.success(request, "User deleted successfully.")

    except Exception as e:
        logger.error(f"Error deleting user: {e}")
        messages.error(request, "An error occurred while deleting the user.")

    return redirect('addUser:show_user')




# - UserProfile
def user_profile(request, user_id):
    profile = get_object_or_404(Member, pk=user_id)

    form = MemberForm(instance=profile)

    return render(request, 'user/user_profile.html', {'form': form, 'user': profile})


