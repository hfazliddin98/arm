from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Viloyat

class ViloyatListView(ListView):
    model = Viloyat
    template_name = 'viloyat/viloyat_list.html'

class ViloyatDetailView(LoginRequiredMixin, DetailView):
    model = Viloyat
    template_name = 'viloyat/viloyat_detail.html'

class ViloyatUpdateView(LoginRequiredMixin, UpdateView):
    model = Viloyat
    # tahrirlash uchun
    template_name = 'viloyat/viloyat_edit.html'
    fields = (
        'viloyat',
    )

class ViloyatDeleteView(LoginRequiredMixin, DeleteView):
    model = Viloyat
    template_name = 'viloyat/viloyat_delete.html'
    success_url = reverse_lazy('viloyat _list')

class ViloyatCreateView(LoginRequiredMixin, CreateView):
    model = Viloyat
    template_name = 'viloyat/viloyat_new.html'
    fields = (
        'viloyat',
        'author',
    )

    
