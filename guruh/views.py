from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Guruh



class GuruhListView(ListView):
    model = Guruh
    template_name = 'guruh/guruh_list.html'

class GuruhDetailView(LoginRequiredMixin, DetailView):
    model = Guruh
    template_name = 'guruh/guruh_detail.html'

class GuruhUpdateView(LoginRequiredMixin, UpdateView):
    model = Guruh
    # tahrirlash uchun
    template_name = 'guruh/guruh_edit.html'
    fields = (
        'guruh',
    )

class GuruhDeleteView(LoginRequiredMixin, DeleteView):
    model = Guruh
    template_name = 'guruh/guruh_delete.html'
    success_url = reverse_lazy('guruh_list')

class GuruhCreateView(LoginRequiredMixin, CreateView):
    model = Guruh
    template_name = 'guruh/guruh_new.html'
    fields = (
        'guruh',
        'author',
    )

    
