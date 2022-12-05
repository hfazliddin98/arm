from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Kafedra

class KafedraListView(ListView):
    model = Kafedra
    template_name = 'kafedra/kafedra_list.html'

class KafedraDetailView(LoginRequiredMixin, DetailView):
    model = Kafedra
    template_name = 'kafedra/kafedra_detail.html'

class KafedraUpdateView(LoginRequiredMixin, UpdateView):
    model = Kafedra
    # tahrirlash uchun
    template_name = 'kafedra/kafedra_edit.html'
    fields = (
        'kafedra',
    )

class KafedraDeleteView(LoginRequiredMixin, DeleteView):
    model = Kafedra
    template_name = 'kafedra/kafedra_delete.html'
    success_url = reverse_lazy('kafedra _list')

class KafedraCreateView(LoginRequiredMixin, CreateView):
    model = Kafedra
    template_name = 'kafedra/kafedra_new.html'
    fields = (
        'kafedra',
        'author',
    )

    
