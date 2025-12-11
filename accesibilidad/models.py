from django.db import models

# Clase 1: Recursos disponibles en el laboratorio
class RecursoAccesibilidad(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True, null=True)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.nombre

# Clase 2: Necesidades o problemas detectados
class Necesidad(models.Model):
    descripcion = models.TextField()
    fecha_reportada = models.DateField(auto_now_add=True)
    solucionada = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.descripcion[:50]}{'...' if len(self.descripcion)>50 else ''}"
