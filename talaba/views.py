from django.contrib.auth.mixins import LoginRequiredMixin
from distutils.command.install_egg_info import safe_name
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from familiya.models import Familiya
from ism.models import Ism
from .models import Talaba
from arm_2.models import Arm_2
from accounts.models import Foydalanuvchi


def talaba(request):
    kitob = Arm_2.objects.all().filter(familya=1)
    ism =Talaba.model.objects.all().filter(familiya=1)
    print(kitob)
    print(ism)
    if kitob == ism:
        return render(request, 'talaba/olgan_kitob.html', {
        'kitob': kitob,
        'familiya': ism,
        
        })
    else:
        er = 'Error'
        return render(request, 'talaba/olgan_kitob.html', {
        'er': er,
        
        
    })


    

    

class TalabaListView(ListView):
    model = Talaba
    template_name = 'talaba/talaba_list.html'

class TalabaBarcha(ListView):
    model = Talaba
    template_name = 'talaba/barcha.html'

class TalabaYangilik(ListView):
    model = Talaba
    template_name = 'talaba/yangilik.html'

class TalabaOlgan(ListView):
    model = Talaba
    template_name = 'talaba/olgan_kitob.html'

class TalabaBuyurtma(ListView):
    model = Talaba
    template_name = 'talaba/buyurtma.html'

class TalabaDetailView(LoginRequiredMixin, DetailView):
    model = Talaba
    template_name = 'talaba/talaba_detail.html'

class TalabaUpdateView(LoginRequiredMixin, UpdateView):
    model = Talaba
    # tahrirlash uchun    
    template_name = 'talaba/talaba_edit.html'
    fields = (
        'familiya', 
        'ism',
        'sharif',
        'tugilgan_kun_oy_yil',
        'fakultet',
        'yonalish',
        'kurs',
        'guruh',  
        'viloyat',
        'tuman',
        'kocha_uy',
        'tel_raqami',
        'pasport_seryasi',
        'pasport_raqami',
               
    )

class TalabaDeleteView(LoginRequiredMixin, DeleteView):
    model = Talaba
    template_name = 'talaba/talaba_delete.html'
    success_url = reverse_lazy('talaba_list')

class TalabaCreateView(LoginRequiredMixin, CreateView):
    model = Talaba
    template_name = 'talaba/talaba_new.html'
    fields = (
        'familiya', 
        'ism',
        'sharif',
        'tugilgan_kun_oy_yil',
        'fakultet',
        'yonalish',
        'kurs',
        'guruh',  
        'viloyat',
        'tuman',
        'kocha_uy',
        'tel_raqami',
        'pasport_seryasi',
        'pasport_raqami', 
        'author',      
    )

    

class Talaba(ListView):
    model = Talaba
    template_name = 'talaba/talaba.html'


