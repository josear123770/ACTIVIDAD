from django.db import models
from django.contrib.auth.models import User # Importamos el modelo User de Django

class EquipoInventario(models.Model):
    """
    Define el modelo para un equipo dentro del sistema de inventario.
    Incluye los campos requeridos para identificación, costo y responsabilidad.
    """
    
    numero_inventario = models.CharField(
        max_length=50,
        unique=True,  
        verbose_name="Número de Inventario"
    )

    
    descripcion = models.TextField(
        verbose_name="Descripción o Nombre del Equipo"
    )

    
    precio_adquisicion = models.DecimalField(
        max_digits=10,  
        decimal_places=2, 
        verbose_name="Precio de Adquisición"
    )

    
    usuario_registro = models.ForeignKey(
        User,
        on_delete=models.CASCADE,  
        related_name='equipos_registrados',  
        verbose_name="Usuario Responsable"
    )

    
    class Meta:
        ordering = ['numero_inventario']
        verbose_name = "Equipo de Inventario"
        verbose_name_plural = "Equipos de Inventario"

    def __str__(self):
        """Devuelve una representación de cadena del objeto."""
        return f"[{self.numero_inventario}] - {self.descripcion[:40]}..."