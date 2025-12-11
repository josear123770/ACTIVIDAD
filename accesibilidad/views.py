from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import RecursoAccesibilidad, Necesidad
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'accesibilidad/index.html'


# ----- RECURSOS -----
class RecursoAccesibilidadListView(ListView):
    model = RecursoAccesibilidad
    template_name = 'accesibilidad/recurso_list.html'

class RecursoAccesibilidadCreateView(CreateView):
    model = RecursoAccesibilidad
    fields = ['nombre', 'descripcion', 'cantidad']
    template_name = 'accesibilidad/recurso_form.html'
    success_url = reverse_lazy('accesibilidad:recurso_listar')

class RecursoAccesibilidadUpdateView(UpdateView):
    model = RecursoAccesibilidad
    fields = ['nombre', 'descripcion', 'cantidad']
    template_name = 'accesibilidad/recurso_form.html'
    success_url = reverse_lazy('accesibilidad:recurso_listar')

class RecursoAccesibilidadDeleteView(DeleteView):
    model = RecursoAccesibilidad
    template_name = 'accesibilidad/recurso_confirm_delete.html'
    success_url = reverse_lazy('accesibilidad:recurso_listar')

# ----- NECESIDADES -----
class NecesidadListView(ListView):
    model = Necesidad
    template_name = 'accesibilidad/necesidad_list.html'

class NecesidadCreateView(CreateView):
    model = Necesidad
    fields = ['descripcion', 'solucionada']
    template_name = 'accesibilidad/necesidad_form.html'
    success_url = reverse_lazy('accesibilidad:necesidad_listar')


class NecesidadUpdateView(UpdateView):
    model = Necesidad
    fields = ['descripcion', 'solucionada']
    template_name = 'accesibilidad/necesidad_form.html'
    success_url = reverse_lazy('accesibilidad:necesidad_listar')

class NecesidadDeleteView(DeleteView):
    model = Necesidad
    template_name = 'accesibilidad/necesidad_confirm_delete.html'
    success_url = reverse_lazy('accesibilidad:necesidad_listar')

class NecesidadDetailView(DetailView):
    model = Necesidad
    template_name = 'accesibilidad/necesidad_detail.html'
