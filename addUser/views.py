from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from .forms import MemberForm

from .models import Member



class AddUser(View):
    template_name = 'users/add_user.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        amana = request.POST.get('amana')
        partyde = request.POST.get('partyde')
        amanaQism = request.POST.get('amanaQism')
        amanaSheyakha = request.POST.get('amanaSheyakha')
        amanaCairo = request.POST.get('amanaCairo')
        amanaKetaa = request.POST.get('amanaKetaa')
        Taam = request.POST.get('Taam')
        specificLagna = request.POST.get('specificLagna')
        pastParty = request.POST.get('pastParty')
        manasebAamma = request.POST.get('manasebAamma')
        sanaDawra = request.POST.get('sanaDawra')
        odwyaSabka = request.POST.get('odwyaSabka')
        name = request.POST.get('name')
        userImg = request.POST.get('userImg')
        presidentPartyName = request.POST.get('presidentPartyName')
        noaaelAdwiaa = request.POST.get('noaaelAdwiaa')
        famousName = request.POST.get('famousName')
        NationalId = request.POST.get('NationalId')
        NationalIdImg = request.POST.get('NationalIdImg')
        age = request.POST.get('age')
        yearBirth = request.POST.get('yearBirth')
        monthBirth = request.POST.get('monthBirth')
        dayBirth = request.POST.get('dayBirth')
        education = request.POST.get('education')
        workProfession = request.POST.get('workProfession')
        nekaba = request.POST.get('nekaba')
        ketaaAamel = request.POST.get('ketaaAamel')
        currentlyWorkProfession = request.POST.get('currentlyWorkProfession')
        martialStatus = request.POST.get('martialStatus')
        mobileOne = request.POST.get('mobileOne')
        mobileTwo = request.POST.get('mobileTwo')
        landline = request.POST.get('landline')
        email = request.POST.get('email')
        rakmElmabna = request.POST.get('rakmElmabna')
        street = request.POST.get('street')
        district = request.POST.get('district')
        city = request.POST.get('city')
        qism = request.POST.get('qism')
        ketaa = request.POST.get('ketaa')
        mohafza = request.POST.get('mohafza')


        user = Member(
            name=name, amana=amana, partyde=partyde, amanaQism=amanaQism,
            amanaSheyakha=amanaSheyakha, amanaCairo=amanaCairo, amanaKetaa=amanaKetaa,
            Taam=Taam, specificLagna=specificLagna, pastParty=pastParty, manasebAamma=manasebAamma,
            sanaDawra=sanaDawra, odwyaSabka=odwyaSabka, userImg=userImg, presidentPartyName=presidentPartyName,
            noaaelAdwiaa=noaaelAdwiaa, famousName=famousName, NationalId=NationalId, NationalIdImg=NationalIdImg,
            age=age, yearBirth=yearBirth,
            monthBirth=monthBirth, dayBirth=dayBirth, education=education, workProfession=workProfession,
            nekaba=nekaba, ketaaAamel=ketaaAamel, currentlyWorkProfession=currentlyWorkProfession,
            martialStatus=martialStatus, mobileOne=mobileOne, mobileTwo=mobileTwo, landline=landline,
            email=email, rakmElmabna=rakmElmabna, street=street, district=district, city=city,
            qism=qism, ketaa=ketaa, mohafza=mohafza,
        )
        user.save()

        return redirect('app:dashboard')


@login_required(login_url='app:login')
def show_user(request, *args, **kwargs):
    users = Member.objects.all()
    context = {'users': users}
    return render(request, 'user/Table.html', context)




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




def delete_user(request, user_id):

    try:
        user = get_object_or_404(Member, pk=user_id)

        user.delete()

        messages.success(request, "User deleted successfully.")

    except Exception as e:
        logger.error(f"Error deleting user: {e}")
        messages.error(request, "An error occurred while deleting the user.")

    return redirect('app:dashboard')



def search_members(request):
    keyword = request.GET.get('keyword', '')
    members = Member.objects.filter(name__icontains=keyword)

    data = {
        'members': [{'name': member.name, 'email': member.email} for member in members]
    }

    return JsonResponse(data)



# def user_profile(request, user_id):
#     profile = get_object_or_404(Member, pk=user_id)
#
#     if request.method == 'GET':
#         form = MemberForm(request.POST, instance=profile)
#         if form.is_valid():
#             form.save()
#     else:
#         form = MemberForm(instance=profile)
#
#     return render(request, 'user/user_profile.html', {'form': form, 'user': profile})




def user_profile(request, user_id):
    profile = get_object_or_404(Member, pk=user_id)

    form = MemberForm(instance=profile)

    return render(request, 'user/user_profile.html', {'form': form, 'user': profile})
