from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Spesa, TipoSpesa
from .forms import SpesaForm, TipoSpesaForm

class HomePageView(ListView):
    template_name = 'home.html'
    model = Spesa

class SpesaDetailView(DetailView):
    model = Spesa
    template_name = 'spesa_detail.html'

class SpesaAddView(CreateView):
    template_name = 'spesa_form.html'
    model = Spesa
    form_class = SpesaForm

class SpesaEditView(UpdateView):
    template_name = 'spesa_form.html'
    model = Spesa
    form_class = SpesaForm

class SpesaDeleteView(DeleteView):
    model = Spesa
    template_name = 'spesa_delete.html'
    success_url = reverse_lazy('home')

class TipoSpesaListView(ListView):
    model = TipoSpesa
    template_name = 'tipo_spesa_list.html'

class TipoSpesaDetailView(DetailView):
    model = TipoSpesa
    template_name = 'tipo_spesa_detail.html'

class TipoSpesaAddView(CreateView):
    model = TipoSpesa
    template_name = 'tipo_spesa_form.html'
    form_class = TipoSpesaForm

class TipoSpesaEditView(UpdateView):
    model = TipoSpesa
    template_name = 'tipo_spesa_form.html'
    form_class = TipoSpesaForm

class TipoSpesaDeleteView(DeleteView):
    model = TipoSpesa
    template_name = 'tipo_spesa_delete.html'
    success_url = reverse_lazy('tipo_spesa_list')
