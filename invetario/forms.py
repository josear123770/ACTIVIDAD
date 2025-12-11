# C:\Users\HP\Grupo5\invetario\forms.py

from django import forms
from .models import EquipoInventario

class EquipoInventarioForm(forms.ModelForm):
    """
    Formulario basado en el modelo EquipoInventario para la creación y edición
    de registros.
    """
    class Meta:
        # 1. Especifica el modelo que usará este formulario
        model = EquipoInventario 
        
        # 2. Indica qué campos del modelo quieres incluir en el formulario
        # (Excluimos 'usuario_registro' porque lo asignaremos automáticamente en views.py)
        fields = ['numero_inventario', 'descripcion', 'precio_adquisicion'] 
        
        # Opcional: Personalizar los labels
        labels = {
            'numero_inventario': 'N° de Inventario',
            'descripcion': 'Descripción del Equipo',
            'precio_adquisicion': 'Precio (€ / $)',
        }