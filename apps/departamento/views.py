from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy


from .forms import DepartamentoForm
from .models import Departamento
# Create your views here.

class DepartamentoList(ListView):
 model = Departamento
 template_name = 'departamento/departamento_list.html'

class DepartamentoCreate(CreateView):
 model = Departamento
 form_class = DepartamentoForm
 template_name = 'departamento/departamento_form.html'
 success_url = reverse_lazy('departamento:departamento_listar')


class DepartamentoUpdate(UpdateView):
 model = Departamento
 form_class = DepartamentoForm
 template_name = 'departamento/departamento_form.html'
 success_url = reverse_lazy('departamento:departamento_listar')


class DepartamentoDelete(DeleteView):
 model = Departamento
 template_name = 'departamento/departamento_delete.html'
 success_url = reverse_lazy('departamento:departamento_listar')
