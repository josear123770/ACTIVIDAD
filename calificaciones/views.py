from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Periodo, Docente, Estudiante, Asignatura, Curso, Clase, Matricula, Nota
from .forms import PeriodoForm, DocenteForm, EstudianteForm, AsignaturaForm, CursoForm, ClaseForm, MatriculaForm, NotaForm
from django.shortcuts import render

def index(request):
    return render(request, 'calificaciones/index.html')



# -------------------- PERIODOS --------------------
class PeriodoCreateView(CreateView):
    model = Periodo
    form_class = PeriodoForm
    template_name = 'calificaciones/periodo_form.html'
    success_url = reverse_lazy('calificaciones:periodo_listar')

class PeriodoListView(ListView):
    model = Periodo
    context_object_name = 'periodos'
    template_name = 'calificaciones/periodo_list.html'

class PeriodoDetailView(DetailView):
    model = Periodo
    context_object_name = 'periodo'
    template_name = 'calificaciones/periodo_detail.html'

class PeriodoUpdateView(UpdateView):
    model = Periodo
    form_class = PeriodoForm
    template_name = 'calificaciones/periodo_form.html'
    success_url = reverse_lazy('calificaciones:periodo_listar')

class PeriodoDeleteView(DeleteView):
    model = Periodo
    template_name = 'calificaciones/periodo_confirm_delete.html'
    success_url = reverse_lazy('calificaciones:periodo_listar')


# -------------------- DOCENTES --------------------
class DocenteCreateView(CreateView):
    model = Docente
    form_class = DocenteForm
    template_name = 'calificaciones/docente_form.html'
    success_url = reverse_lazy('calificaciones:docente_listar')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class DocenteListView(ListView):
    model = Docente
    context_object_name = 'docentes'
    template_name = 'calificaciones/docente_list.html'

class DocenteDetailView(DetailView):
    model = Docente
    context_object_name = 'docente'
    template_name = 'calificaciones/docente_detail.html'

class DocenteUpdateView(UpdateView):
    model = Docente
    form_class = DocenteForm
    template_name = 'calificaciones/docente_form.html'
    success_url = reverse_lazy('calificaciones:docente_listar')

class DocenteDeleteView(DeleteView):
    model = Docente
    template_name = 'calificaciones/docente_confirm_delete.html'
    success_url = reverse_lazy('calificaciones:docente_listar')


# -------------------- ESTUDIANTES --------------------
class EstudianteCreateView(CreateView):
    model = Estudiante
    form_class = EstudianteForm
    template_name = 'calificaciones/estudiante_form.html'
    success_url = reverse_lazy('calificaciones:estudiante_listar')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class EstudianteListView(ListView):
    model = Estudiante
    context_object_name = 'estudiantes'
    template_name = 'calificaciones/estudiante_list.html'

class EstudianteDetailView(DetailView):
    model = Estudiante
    context_object_name = 'estudiante'
    template_name = 'calificaciones/estudiante_detail.html'

class EstudianteUpdateView(UpdateView):
    model = Estudiante
    form_class = EstudianteForm
    template_name = 'calificaciones/estudiante_form.html'
    success_url = reverse_lazy('calificaciones:estudiante_listar')

class EstudianteDeleteView(DeleteView):
    model = Estudiante
    template_name = 'calificaciones/estudiante_confirm_delete.html'
    success_url = reverse_lazy('calificaciones:estudiante_listar')


# -------------------- ASIGNATURAS --------------------
class AsignaturaCreateView(CreateView):
    model = Asignatura
    form_class = AsignaturaForm
    template_name = 'calificaciones/asignatura_form.html'
    success_url = reverse_lazy('calificaciones:asignatura_listar')

class AsignaturaListView(ListView):
    model = Asignatura
    context_object_name = 'asignaturas'
    template_name = 'calificaciones/asignatura_list.html'

class AsignaturaDetailView(DetailView):
    model = Asignatura
    context_object_name = 'asignatura'
    template_name = 'calificaciones/asignatura_detail.html'

class AsignaturaUpdateView(UpdateView):
    model = Asignatura
    form_class = AsignaturaForm
    template_name = 'calificaciones/asignatura_form.html'
    success_url = reverse_lazy('calificaciones:asignatura_listar')

class AsignaturaDeleteView(DeleteView):
    model = Asignatura
    template_name = 'calificaciones/asignatura_confirm_delete.html'
    success_url = reverse_lazy('calificaciones:asignatura_listar')


# -------------------- CURSOS --------------------
class CursoCreateView(CreateView):
    model = Curso
    form_class = CursoForm
    template_name = 'calificaciones/curso_form.html'
    success_url = reverse_lazy('calificaciones:curso_listar')

class CursoListView(ListView):
    model = Curso
    context_object_name = 'cursos'
    template_name = 'calificaciones/curso_list.html'

class CursoDetailView(DetailView):
    model = Curso
    context_object_name = 'curso'
    template_name = 'calificaciones/curso_detail.html'

class CursoUpdateView(UpdateView):
    model = Curso
    form_class = CursoForm
    template_name = 'calificaciones/curso_form.html'
    success_url = reverse_lazy('calificaciones:curso_listar')

class CursoDeleteView(DeleteView):
    model = Curso
    template_name = 'calificaciones/curso_confirm_delete.html'
    success_url = reverse_lazy('calificaciones:curso_listar')


# -------------------- CLASES --------------------
class ClaseCreateView(CreateView):
    model = Clase
    form_class = ClaseForm
    template_name = 'calificaciones/clase_form.html'
    success_url = reverse_lazy('calificaciones:clase_listar')

class ClaseListView(ListView):
    model = Clase
    context_object_name = 'clases'
    template_name = 'calificaciones/clase_list.html'

class ClaseDetailView(DetailView):
    model = Clase
    context_object_name = 'clase'
    template_name = 'calificaciones/clase_detail.html'

class ClaseUpdateView(UpdateView):
    model = Clase
    form_class = ClaseForm
    template_name = 'calificaciones/clase_form.html'
    success_url = reverse_lazy('calificaciones:clase_listar')

class ClaseDeleteView(DeleteView):
    model = Clase
    template_name = 'calificaciones/clase_confirm_delete.html'
    success_url = reverse_lazy('calificaciones:clase_listar')


# -------------------- MATRÍCULAS --------------------
class MatriculaCreateView(CreateView):
    model = Matricula
    form_class = MatriculaForm
    template_name = 'calificaciones/matricula_form.html'
    success_url = reverse_lazy('calificaciones:matricula_listar')

class MatriculaListView(ListView):
    model = Matricula
    context_object_name = 'matriculas'
    template_name = 'calificaciones/matricula_list.html'

class MatriculaDetailView(DetailView):
    model = Matricula
    context_object_name = 'matricula'
    template_name = 'calificaciones/matricula_detail.html'

class MatriculaUpdateView(UpdateView):
    model = Matricula
    form_class = MatriculaForm
    template_name = 'calificaciones/matricula_form.html'
    success_url = reverse_lazy('calificaciones:matricula_listar')

class MatriculaDeleteView(DeleteView):
    model = Matricula
    template_name = 'calificaciones/matricula_confirm_delete.html'
    success_url = reverse_lazy('calificaciones:matricula_listar')


# -------------------- NOTAS --------------------
class NotaCreateView(CreateView):
    model = Nota
    form_class = NotaForm
    template_name = 'calificaciones/nota_form.html'
    success_url = reverse_lazy('calificaciones:nota_listar')

class NotaListView(ListView):
    model = Nota
    context_object_name = 'notas'
    template_name = 'calificaciones/nota_list.html'

class NotaDetailView(DetailView):
    model = Nota
    context_object_name = 'nota'
    template_name = 'calificaciones/nota_detail.html'

class NotaUpdateView(UpdateView):
    model = Nota
    form_class = NotaForm
    template_name = 'calificaciones/nota_form.html'
    success_url = reverse_lazy('calificaciones:nota_listar')

class NotaDeleteView(DeleteView):
    model = Nota
    template_name = 'calificaciones/nota_confirm_delete.html'
    success_url = reverse_lazy('calificaciones:nota_listar')
