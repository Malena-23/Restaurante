from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import MesasEstado, Mesa
from .forms import MesasEstadoForm, MesaForm

class MesasEstadoListView(LoginRequiredMixin, ListView):
    model = MesasEstado
    template_name = 'mesas_estado/mesas_estado_list.html'
    context_object_name = 'mesas_estado'
    
class MesasEstadoCreateView(LoginRequiredMixin, CreateView):
    model = MesasEstado
    form_class = MesasEstadoForm
    template_name = 'mesas_estado/mesas_estado_form.html'
    success_url = '/mesas/mesas_estado/'
    
class MesasEstadoUpdateView(LoginRequiredMixin, UpdateView):
    model = MesasEstado
    form_class = MesasEstadoForm
    template_name = 'mesas_estado/mesas_estado_edit_form.html'
    success_url = '/mesas/mesas_estado/'
    
class MesasEstadoDeleteView(LoginRequiredMixin, DeleteView):    
    model = MesasEstado
    template_name = 'mesas_estado/mesas_estado_confirm_delete.html'
    success_url = '/mesas/mesas_estado/'

class MesaListView(LoginRequiredMixin, ListView):
    model = Mesa
    template_name = 'mesas/mesas_list.html'
    context_object_name = 'mesas'
    
class MesaCreateView(LoginRequiredMixin, CreateView):
    model = Mesa
    form_class = MesaForm
    template_name = 'mesas/mesas_form.html'
    success_url = '/mesas/mesas/'
    
class MesaUpdateView(LoginRequiredMixin, UpdateView):
    model = Mesa
    form_class = MesaForm
    template_name = 'mesas/mesas_edit_form.html'
    success_url = '/mesas/mesas/'
    
class MesaDeleteView(LoginRequiredMixin, DeleteView):
    model = Mesa
    template_name = 'mesas/mesas_confirm_delete.html'
    success_url = '/mesas/mesas/'
