from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Spesa
from .forms import SpesaAddForm

class HomePageView(ListView):
    template_name = 'home.html'
    model = Spesa

class SpesaDetailView(DetailView):
    model = Spesa
    template_name = 'spesa_detail.html'

class SpesaAddView(CreateView):
    template_name = 'spesa_add.html'
    model = Spesa
    form_class = SpesaAddForm

class SpesaDeleteView(DeleteView):
    model = Spesa
    template_name = 'spesa_delete.html'
    success_url = reverse_lazy('home')
