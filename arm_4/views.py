from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Arm_4

class Arm_4HListView(ListView):
    model = Arm_4
    template_name = 'arm_1/arm.html'

class Arm_4ListView(ListView):
    model = Arm_4
    template_name = 'arm_4/arm_4_list.html'

class Arm_4DetailView(LoginRequiredMixin, DetailView):
    model = Arm_4
    template_name = 'arm_4/arm_4_detail.html'

class Arm_4UpdateView(LoginRequiredMixin, UpdateView):
    model = Arm_4
    # tahrirlash uchun    
    template_name = 'arm_4/arm_4_edit.html'
    fields = (
        'fan',
        'adabiyot',
        'mualif',
        'qollanma',                
    )

class Arm_4DeleteView(LoginRequiredMixin, DeleteView):
    model = Arm_4
    template_name = 'arm_4/arm_4_delete.html'
    success_url = reverse_lazy('arm_4_list')

class Arm_4CreateView(LoginRequiredMixin, CreateView):
    model = Arm_4
    template_name = 'arm_4/arm_4_new.html'
    fields = (
        'fan',
        'adabiyot',
        'mualif',
        'qollanma',
        'author',       
    )

    
