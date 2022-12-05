from datetime import datetime
from accounts.models import Foydalanuvchi
from arm_1.models import Arm_1
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from familiya.models import Familiya
from arm_1.models import Arm_1
from .models import Arm_2, Talaba_kitob
from .forms import Talaba_kitobForm



def kitob_list(request, kitob_id):
    kitob = Talaba_kitob.objects.get(pk=kitob_id)
    return render(request, 'arm_2/kitob-list.html', {
            'kitob': kitob,            
    })


    

def talaba_list(request):
    talaba_list = Arm_2.objects.all()
    return render(request, 'arm_2/talaba-list.html', {
        'talaba_list': talaba_list,            
    })



def talaba_javob(request):
    # javob_list = Talaba_kitob.objects.filter(familya=1).all()
    hatamov = Talaba_kitob.objects.filter(ism=1).values('familya')[0]
    fazliddin = Arm_2.objects.filter(ism=1).values('familya')[0]
    # yodgorov = Talaba_kitob.objects.filter(familya=1)[1]
    yodgorov = Talaba_kitob.objects.values('familya')[3]
    azamjon = Arm_2.objects.values('familya')[1]
    jorayev = Talaba_kitob.objects.get(kitob__contains='daryo')
    muzaffar = Arm_2.objects.values('familya')[2]
    user = Foydalanuvchi.objects.values('familiya_a')[7]
    ha = Familiya.objects.values('familiya')[0]
    print(hatamov)
    print(fazliddin)
    print(yodgorov)
    print(azamjon)
    print(jorayev)
    print(muzaffar)
    print(user)
    print(ha)
    

    if hatamov == fazliddin:
        hatamov = Talaba_kitob.objects.filter(familya=1).filter(ism=1).all()
        ha = Talaba_kitob.objects.filter(familya=1).filter(ism=1)[1]
        print(hatamov)
        return render(request, 'arm_2/talaba-javob.html', {
            'javob_list': hatamov,
            'ha':ha,
        })
    if yodgorov == azamjon:
        yodgorov = Talaba_kitob.objects.filter(familya=2).filter(id=8).order_by('familya')
        print(yodgorov)
        return render(request, 'arm_2/talaba-javob.html', {
            'javob_list': yodgorov,
        })
    if jorayev == muzaffar:
        javob_list = Talaba_kitob.objects.filter(familya=3).filter(id=9).order_by('familya')
        print(javob_list)
        return render(request, 'arm_2/talaba-javob.html', {
            'javob_list': javob_list,
        })


    else:
        javob_list = 'Error'
        return render(request, 'arm_2/talaba-javob.html', {
            'javob_list': javob_list,            
        })

def talaba_kitob(request):
    submitted = False
    if request.method == 'POST':
        talaba = Talaba_kitobForm(request.POST)
        if talaba.is_valid():
            talaba.save()
            return HttpResponseRedirect('/arm-2/talaba-kitob/?submitted=True')
    else:
        talaba = Talaba_kitobForm
        if 'submitted' in request.GET:
            submitted = True


    return render(request, 'arm_2/talaba-kitob.html', {
        'talaba': talaba,
        'submitted': submitted,
    })
# malumotlari bo`yicha filterlash
def javob(request):
    ja = Arm_2.objects.filter(kurs=1).filter(guruh=1).filter(ism=1).all()
    us =Arm_2.objects.filter(familya=1).filter(author=1).all()
    vaqt = datetime.now()

    #auth = form.instance.author
    print(us)
    #print(foy)
    #print(auth)
    def foydalanuvchi(self, form):
        foy = self.request.user
        print(foy)
        return super(foy)
    return render(request, 'arm_2/javob.html', {
        'ja': ja ,
        'vaqt': vaqt ,
        'us': us ,
    })

    def foydalanuvchi(self, form):
        foy = self.request.user
        print(foy)
        return super().foydalanuvchi(form)





class Arm_2ListView(ListView):
    model = Arm_2
    # list holatda ko`rsatish uchun
    template_name = 'arm_2/arm_2_list.html'

class Arm_2sinov(ListView):
    model = Arm_2
    # list holatda ko`rsatish uchun
    template_name = 'arm_2/arm_2.html'

class Arm_2DetailView(LoginRequiredMixin, DetailView):
    model = Arm_2
    # ekranga chiqrish uchun
    template_name = 'arm_2/arm_2_detail.html'

class Arm_2UpdateView(LoginRequiredMixin, UpdateView):
    model = Arm_2
    # tahrirlash uchun
    template_name = 'arm_2/arm_2_edit.html'
    fields = (
        'formulyar_raqami',
        'darajasi',
        'fakultet',
        'yonalish',
        'kurs',
        'guruh',
        'familya',
        'ism',
        'sharifi',
        'tugilgan_kun_oy_yil',
        'viloyat',
        'tuman',
        'kocha_uy',
        'tel_raqami',
        'pasport_seryasi',
        'pasport_raqami',
    )

class Arm_2DeleteView(LoginRequiredMixin, DeleteView):
    model = Arm_2
    # o`chirrish uchun
    template_name = 'arm_2/arm_2_delete.html'
    success_url = reverse_lazy('arm_2_list')

class Arm_2CreateView(LoginRequiredMixin, CreateView):
    model = Arm_2
    # yangi malumot kiritish uchun
    template_name = 'arm_2/arm_2_new.html'
    fields = (
        'formulyar_raqami',
        'darajasi',
        'fakultet',
        'yonalish',
        'kurs',
        'guruh',
        'familya',
        'ism',
        'sharifi',
        'tugilgan_kun_oy_yil',
        'viloyat',
        'tuman',
        'kocha_uy',
        'tel_raqami',
        'pasport_seryasi',
        'pasport_raqami',
        'author',
    )
