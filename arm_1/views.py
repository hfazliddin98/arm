from django.contrib.auth.mixins import LoginRequiredMixin
# sayt himoyasi
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Arm_1


# asl nushadagi kitoblarni kiritish uchun

class Arm_1ListView(ListView):
    model = Arm_1
    template_name = 'arm_1/arm_1_list.html'

class Arm_1DetailView(DetailView):
    model = Arm_1
    template_name = 'arm_1/arm_1_detail.html'

class Arm_1UpdateView(LoginRequiredMixin, UpdateView):
    model = Arm_1
    # tahrirlash uchun    
    template_name = 'arm_1/arm_1_edit.html'
    fields = (
        'shifr', 
        'aftor_belgisi', 
        'invertor_nomeri', 
        'mualiflar', 
        'kitob_nomi', 
        'nashriyot', 
        'nashr_yili',
        'isbn',
        'kitob_narxi',
        'tili',
        'alfabit',
        'darslik_turi',
        'kitobni_fondagi_soni',
        'anatatsiya',
        'mundarija',
        'kitob_turi',
        'kitob_rasmini_kiriting',
        'fayl',        
    )

class Arm_1DeleteView(LoginRequiredMixin, DeleteView):
    model = Arm_1
    template_name = 'arm_1/arm_1_delete.html'
    success_url = reverse_lazy('arm_1_list')

class Arm_1CreateView(LoginRequiredMixin, CreateView):
    model = Arm_1
    template_name = 'arm_1/arm_1_new.html'
    fields = (
        'shifr', 
        'aftor_belgisi', 
        'invertor_nomeri', 
        'mualiflar', 
        'kitob_nomi', 
        'nashriyot', 
        'nashr_yili',
        'isbn',
        'kitob_narxi',
        'tili',
        'alfabit',
        'darslik_turi',
        'kitobni_fondagi_soni',
        'anatatsiya',
        'mundarija',
        'kitob_turi',
        'kitob_rasmini_kiriting',
        'fayl', 
        'author',       
    )

    # qoshimcha ulr orqali hujumlar uchun saytga kirmagan foydalanuvchi uchun
    

    
