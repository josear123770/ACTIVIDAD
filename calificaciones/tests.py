from django.test import TestCase
from django.contrib.auth.models import User
from .models import Estudiante, Curso, Periodo, Docente

class EstudianteModelTest(TestCase):
    def setUp(self):
        user = User.objects.create(username="juan", password="1234")
        self.estudiante = Estudiante.objects.create(
            user=user,
            cedula="1234567890",
            fecha_nacimiento="2000-01-01",
            direccion="Calle 123"
        )

    def test_estudiante_str(self):
        self.assertEqual(str(self.estudiante), self.estudiante.user.username)

class CursoModelTest(TestCase):
    def setUp(self):
        periodo = Periodo.objects.create(nombre="2025", fecha_inicio="2025-01-01", fecha_fin="2025-12-31")
        self.curso = Curso.objects.create(nombre="Matemáticas", paralelo="A", periodo=periodo)

    def test_curso_str(self):
        self.assertIn("Matemáticas", str(self.curso))
