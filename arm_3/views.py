from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Arm_3

class Arm_3ListView(ListView):
    model = Arm_3
    template_name = 'arm_3/arm_3_list.html'

class Arm_3DetailView(LoginRequiredMixin, DetailView):
    model = Arm_3
    template_name = 'arm_3/arm_3_detail.html'

class Arm_3UpdateView(LoginRequiredMixin, UpdateView):
    model = Arm_3
    # tahrirlash uchun    
    template_name = 'arm_3/arm_3_edit.html'
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
        'fayl',        
    )

class Arm_3DeleteView(LoginRequiredMixin, DeleteView):
    model = Arm_3
    template_name = 'arm_3/arm_3_delete.html'
    success_url = reverse_lazy('arm_3_list')

class Arm_3CreateView(LoginRequiredMixin, CreateView):
    model = Arm_3
    template_name = 'arm_3/arm_3_new.html'
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
        'fayl',  
        'author',      
    )

    