from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Member
from django.db import connection


class AddUser(View):
    template_name = 'users/add_user.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        record = Member.objects.all()
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

        print(record)

        user = Member(
            name=name, amana=amana, partyde=partyde, amanaQism=amanaQism,
            amanaSheyakha=amanaSheyakha, amanaCairo=amanaCairo, amanaKetaa=amanaKetaa,
            Taam=Taam, specificLagna=specificLagna, pastParty=pastParty, manasebAamma=manasebAamma,
            sanaDawra=sanaDawra, odwyaSabka=odwyaSabka, userImg=userImg, presidentPartyName=presidentPartyName,
            noaaelAdwiaa=noaaelAdwiaa, famousName=famousName, NationalId=NationalId, age=age, yearBirth=yearBirth,
            monthBirth=monthBirth, dayBirth=dayBirth, education=education, workProfession=workProfession,
            nekaba=nekaba, ketaaAamel=ketaaAamel, currentlyWorkProfession=currentlyWorkProfession,
            martialStatus=martialStatus, mobileOne=mobileOne, mobileTwo=mobileTwo, landline=landline,
            email=email, rakmElmabna=rakmElmabna, street=street, district=district, city=city,
            qism=qism, ketaa=ketaa, mohafza=mohafza,
        )
        user.save()

        return redirect('app:dashboard')


class UserList(View):
    template_name = 'user/Table.html'

    def get(self, request, *args, **kwargs):
        users = Member.objects.all()
        print(users)
        context = {'users': users}
        return render(request, self.template_name, context)
