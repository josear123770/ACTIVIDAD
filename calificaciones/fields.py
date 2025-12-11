from django import forms
from .models import Periodo, Docente, Estudiante, Asignatura, Curso, Clase, Matricula, Nota

# ------------------------
# FORMULARIOS
# ------------------------

class PeriodoForm(forms.ModelForm):
    class Meta:
        model = Periodo
        fields = '__all__'
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
        }

class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = '__all__'

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }

class AsignaturaForm(forms.ModelForm):
    class Meta:
        model = Asignatura
        fields = '__all__'

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'

class ClaseForm(forms.ModelForm):
    class Meta:
        model = Clase
        fields = '__all__'

class MatriculaForm(forms.ModelForm):
    class Meta:
        model = Matricula
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }

class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = '__all__'