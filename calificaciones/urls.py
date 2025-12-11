from django.urls import path
from . import views

app_name = 'calificaciones'

urlpatterns = [
    
    path('', views.index, name='index'),  
    # -------------------- PERIODOS --------------------
    path('periodos/', views.PeriodoListView.as_view(), name='periodo_listar'),
    path('periodos/crear/', views.PeriodoCreateView.as_view(), name='periodo_crear'),
    path('periodos/<int:pk>/', views.PeriodoDetailView.as_view(), name='periodo_detalle'),
    path('periodos/<int:pk>/editar/', views.PeriodoUpdateView.as_view(), name='periodo_editar'),
    path('periodos/<int:pk>/eliminar/', views.PeriodoDeleteView.as_view(), name='periodo_eliminar'),

    # -------------------- DOCENTES --------------------
    path('docentes/', views.DocenteListView.as_view(), name='docente_listar'),
    path('docentes/crear/', views.DocenteCreateView.as_view(), name='docente_crear'),
    path('docentes/<int:pk>/', views.DocenteDetailView.as_view(), name='docente_detalle'),
    path('docentes/<int:pk>/editar/', views.DocenteUpdateView.as_view(), name='docente_editar'),
    path('docentes/<int:pk>/eliminar/', views.DocenteDeleteView.as_view(), name='docente_eliminar'),

    # -------------------- ESTUDIANTES --------------------
    path('estudiantes/', views.EstudianteListView.as_view(), name='estudiante_listar'),
    path('estudiantes/crear/', views.EstudianteCreateView.as_view(), name='estudiante_crear'),
    path('estudiantes/<int:pk>/', views.EstudianteDetailView.as_view(), name='estudiante_detalle'),
    path('estudiantes/<int:pk>/editar/', views.EstudianteUpdateView.as_view(), name='estudiante_editar'),
    path('estudiantes/<int:pk>/eliminar/', views.EstudianteDeleteView.as_view(), name='estudiante_eliminar'),

    # -------------------- ASIGNATURAS --------------------
    path('asignaturas/', views.AsignaturaListView.as_view(), name='asignatura_listar'),
    path('asignaturas/crear/', views.AsignaturaCreateView.as_view(), name='asignatura_crear'),
    path('asignaturas/<int:pk>/', views.AsignaturaDetailView.as_view(), name='asignatura_detalle'),
    path('asignaturas/<int:pk>/editar/', views.AsignaturaUpdateView.as_view(), name='asignatura_editar'),
    path('asignaturas/<int:pk>/eliminar/', views.AsignaturaDeleteView.as_view(), name='asignatura_eliminar'),

    # -------------------- CURSOS --------------------
    path('cursos/', views.CursoListView.as_view(), name='curso_listar'),
    path('cursos/crear/', views.CursoCreateView.as_view(), name='curso_crear'),
    path('cursos/<int:pk>/', views.CursoDetailView.as_view(), name='curso_detalle'),
    path('cursos/<int:pk>/editar/', views.CursoUpdateView.as_view(), name='curso_editar'),
    path('cursos/<int:pk>/eliminar/', views.CursoDeleteView.as_view(), name='curso_eliminar'),

    # -------------------- CLASES --------------------
    path('clases/', views.ClaseListView.as_view(), name='clase_listar'),
    path('clases/crear/', views.ClaseCreateView.as_view(), name='clase_crear'),
    path('clases/<int:pk>/', views.ClaseDetailView.as_view(), name='clase_detalle'),
    path('clases/<int:pk>/editar/', views.ClaseUpdateView.as_view(), name='clase_editar'),
    path('clases/<int:pk>/eliminar/', views.ClaseDeleteView.as_view(), name='clase_eliminar'),

    # -------------------- MATRÍCULAS --------------------
    path('matriculas/', views.MatriculaListView.as_view(), name='matricula_listar'),
    path('matriculas/crear/', views.MatriculaCreateView.as_view(), name='matricula_crear'),
    path('matriculas/<int:pk>/', views.MatriculaDetailView.as_view(), name='matricula_detalle'),
    path('matriculas/<int:pk>/editar/', views.MatriculaUpdateView.as_view(), name='matricula_editar'),
    path('matriculas/<int:pk>/eliminar/', views.MatriculaDeleteView.as_view(), name='matricula_eliminar'),

    # -------------------- NOTAS --------------------
    path('notas/', views.NotaListView.as_view(), name='nota_listar'),
    path('notas/crear/', views.NotaCreateView.as_view(), name='nota_crear'),
    path('notas/<int:pk>/', views.NotaDetailView.as_view(), name='nota_detalle'),
    path('notas/<int:pk>/editar/', views.NotaUpdateView.as_view(), name='nota_editar'),
    path('notas/<int:pk>/eliminar/', views.NotaDeleteView.as_view(), name='nota_eliminar'),
]
