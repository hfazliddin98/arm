from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Familiya

class FamiliyaListView(ListView):
    model = Familiya
    template_name = 'familiya/familiya_list.html'

class FamiliyaDetailView(LoginRequiredMixin, DetailView):
    model = Familiya
    template_name = 'familiya/familiya_detail.html'

class FamiliyaUpdateView(LoginRequiredMixin, UpdateView):
    model = Familiya
    # tahrirlash uchun
    template_name = 'familiya/familiya_edit.html'
    fields = (
        'familiya',
    )

class FamiliyaDeleteView(LoginRequiredMixin, DeleteView):
    model = Familiya
    template_name = 'familiya/familiya_delete.html'
    success_url = reverse_lazy('familiya _list')

class FamiliyaCreateView(LoginRequiredMixin, CreateView):
    model = Familiya
    template_name = 'familiya/familiya_new.html'
    fields = (
        'familiya',
        'author',        
    )
