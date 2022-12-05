from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Sharif

class SharifListView(ListView):
    model = Sharif
    template_name = 'sharif/sharif_list.html'

class SharifDetailView(LoginRequiredMixin, DetailView):
    model = Sharif
    template_name = 'sharif/sharif_detail.html'

class SharifUpdateView(LoginRequiredMixin, UpdateView):
    model = Sharif
    # tahrirlash uchun
    template_name = 'sharif/sharif_edit.html'
    fields = (
        'sharif',
    )

class SharifDeleteView(LoginRequiredMixin, DeleteView):
    model = Sharif
    template_name = 'sharif/sharif_delete.html'
    success_url = reverse_lazy('sharif _list')

class SharifCreateView(LoginRequiredMixin, CreateView):
    model = Sharif
    template_name = 'sharif/sharif_new.html'
    fields = (
        'sharif',
        'author',
    )

    
