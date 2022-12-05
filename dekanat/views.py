from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Dekanat


class Dekanat(ListView):
    model = Dekanat
    template_name = 'dekanat/dekanat.html'


