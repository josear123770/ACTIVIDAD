from django.db import models
from django.contrib.auth.models import User

class Periodo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return self.nombre
    
class Docente(models.Model):
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    titulo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    

class Estudiante(models.Model):
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    cedula = models.CharField(max_length=20, unique=True)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Asignatura(models.Model):
    nombre = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    paralelo = models.CharField(max_length=5, default='A')
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} - {self.paralelo} ({self.periodo})"

class Clase(models.Model):
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.asignatura} - {self.curso} - {self.docente}"

class Matricula(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    fecha = models.DateField()

    def __str__(self):
        return f"{self.estudiante} en {self.curso}"

class Nota(models.Model):
    matricula = models.ForeignKey(Matricula, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    trimestre1 = models.FloatField(default=0)
    trimestre2 = models.FloatField(default=0)
    trimestre3 = models.FloatField(default=0)
    promedio = models.FloatField(default=0)

    def calcular_promedio(self):
        return round((self.trimestre1 + self.trimestre2 + self.trimestre3) / 3, 2)

    def save(self, *args, **kwargs):
        self.promedio = self.calcular_promedio()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Notas de {self.matricula.estudiante} ({self.asignatura})"
