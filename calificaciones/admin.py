from django.contrib import admin
from .models import (
    Periodo,
    Docente,
    Estudiante,
    Asignatura,
    Curso,
    Clase,
    Matricula,
    Nota
)

# Registrando modelos en el admin
@admin.register(Periodo)
class PeriodoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_inicio', 'fecha_fin')
    search_fields = ('nombre',)

@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'titulo', 'telefono')
    search_fields = ('nombre', 'apellido', 'titulo')

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'cedula', 'fecha_nacimiento', 'direccion')
    search_fields = ('nombre', 'apellido', 'cedula')

@admin.register(Asignatura)
class AsignaturaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'paralelo', 'periodo')
    list_filter = ('periodo',)
    search_fields = ('nombre', 'paralelo')

@admin.register(Clase)
class ClaseAdmin(admin.ModelAdmin):
    list_display = ('asignatura', 'curso', 'docente')
    list_filter = ('curso', 'docente')
    search_fields = ('asignatura__nombre', 'docente__nombre', 'docente__apellido')

@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'curso', 'periodo', 'fecha')
    list_filter = ('curso', 'periodo')
    search_fields = ('estudiante__nombre', 'estudiante__apellido', 'estudiante__cedula')

@admin.register(Nota)
class NotaAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'asignatura', 'promedio')
    list_filter = ('asignatura',)
