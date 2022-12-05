from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Yonalish

class YonalishListView(ListView):
    model = Yonalish
    template_name = 'yonalish/yonalish_list.html'

class YonalishDetailView(LoginRequiredMixin, DetailView):
    model = Yonalish
    template_name = 'yonalish/yonalish_detail.html'

class YonalishUpdateView(LoginRequiredMixin, UpdateView):
    model = Yonalish
    # tahrirlash uchun
    template_name = 'yonalish/yonalish_edit.html'
    fields = (
        'yonalish',
    )

class YonalishDeleteView(LoginRequiredMixin, DeleteView):
    model = Yonalish
    template_name = 'yonalish/yonalish_delete.html'
    success_url = reverse_lazy('yonalish_list')

class YonalishCreateView(LoginRequiredMixin, CreateView):
    model = Yonalish
    template_name = 'yonalish/yonalish_new.html'
    fields = (
        'yonalish',
        'author',
    )


    
