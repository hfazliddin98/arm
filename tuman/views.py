from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Tuman

class TumanListView(ListView):
    model = Tuman
    template_name = 'tuman/tuman_list.html'

class TumanDetailView(DetailView):
    model = Tuman
    template_name = 'tuman/tuman_detail.html'

class TumanUpdateView(UpdateView):
    model = Tuman
    # tahrirlash uchun    
    template_name = 'tuman/tuman_edit.html'
    fields = (
        'tuman',           
    )

class TumanDeleteView(DeleteView):
    model = Tuman
    template_name = 'tuman/tuman_delete.html'
    success_url = reverse_lazy('tuman _list')

class TumanCreateView(CreateView):
    model = Tuman
    template_name = 'tuman/tuman_new.html'
    fields = (
        'tuman',
        'author'
    )