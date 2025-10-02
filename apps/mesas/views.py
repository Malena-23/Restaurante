from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Categoria, Platillo, Mesa
from .forms import CategoriaForm, PlatilloForm, MesaForm

class CategoriaListView(LoginRequiredMixin, ListView):
    model = Categoria
    template_name = 'categorias/categoria_list.html'
    context_object_name = 'categorias'
    
class CategoriaCreateView(LoginRequiredMixin, CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categorias/categoria_form.html'
    success_url = '/platillos/categorias/'

class CategoriaUpdateView(LoginRequiredMixin, UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categorias/categoria_edit_form.html'
    success_url = '/platillos/categorias/'

class CategoriaDeleteView(LoginRequiredMixin, DeleteView):
    model = Categoria
    template_name = 'categorias/categoria_confirm_delete.html'
    success_url = '/platillos/categorias/'
    
class PlatilloListView(LoginRequiredMixin, ListView):
    model = Platillo
    template_name = 'platillos/platillos_list.html'
    context_object_name = 'platillos'
    
class PlatilloCreateView(LoginRequiredMixin, CreateView):
    model = Platillo
    form_class = PlatilloForm
    template_name = 'platillos/platillos_form.html'
    success_url = '/platillos/platillos/'
    
class PlatilloUpdateView(LoginRequiredMixin, UpdateView):
    model = Platillo
    form_class = PlatilloForm
    template_name = 'platillos/platillos_edit_form.html'
    success_url = '/platillos/platillos/'
    
class PlatilloDeleteView(LoginRequiredMixin, DeleteView):
    model = Platillo
    template_name = 'platillos/platillos_confirm_delete.html'
    success_url = '/platillos/platillos/'
    
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
