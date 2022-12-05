from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Ism

class IsmListView(ListView):
    model = Ism
    template_name = 'ism/ism_list.html'

class IsmDetailView(LoginRequiredMixin, DetailView):
    model = Ism
    template_name = 'ism/ism_detail.html'

class IsmUpdateView(LoginRequiredMixin, UpdateView):
    model = Ism
    # tahrirlash uchun
    template_name = 'ism/ism_edit.html'
    fields = (
        'ism',
    )

class IsmDeleteView(LoginRequiredMixin, DeleteView):
    model = Ism
    template_name = 'ism/ism_delete.html'
    success_url = reverse_lazy('ism _list')

class IsmCreateView(LoginRequiredMixin, CreateView):
    model = Ism
    template_name = 'ism/ism_new.html'
    fields = (
        'ism',
        'author',
    )

    
