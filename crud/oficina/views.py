from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Oficina


class OficinaListView(ListView):
    model = Oficina
    template_name = "oficina/lista.html"
    context_object_name = "oficinas"

class OficinaDetailView(DetailView):
    model = Oficina
    template_name = "oficina/detalle.html"
    context_object_name = "oficina"

class OficinaCreateView(CreateView):
    model = Oficina
    template_name = "oficina/crear.html"
    fields = ['nombre', 'nombreCorto']
    success_url = reverse_lazy('oficina:lista')

class OficinaUpdateView(UpdateView):
    model = Oficina
    template_name = "oficina/crear.html"
    fields = ['nombre', 'nombreCorto']
    success_url = reverse_lazy('oficina:lista')

class OficinaDeleteView(DeleteView):
    model = Oficina
    template_name = "oficina/eliminar.html"
    success_url = reverse_lazy('oficina:lista')
    context_object_name = "oficina"