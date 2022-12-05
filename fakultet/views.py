from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Fakultet

class FakultetListView(ListView):
    model = Fakultet
    template_name = 'fakultet/fakultet_list.html'

class FakultetDetailView(LoginRequiredMixin, DetailView):
    model = Fakultet
    template_name = 'fakultet/fakultet_detail.html'

class FakultetUpdateView(LoginRequiredMixin, UpdateView):
    model = Fakultet
    # tahrirlash uchun
    template_name = 'fakultet/fakultet_edit.html'
    fields = (
        'fakultet',
    )

class FakultetDeleteView(LoginRequiredMixin, DeleteView):
    model = Fakultet
    template_name = 'fakultet/fakultet_delete.html'
    success_url = reverse_lazy('fakultet _list')

class FakultetCreateView(LoginRequiredMixin, CreateView):
    model = Fakultet
    template_name = 'fakultet/fakultet_new.html'
    fields = (
        'fakultet',
        'author',    
    )
