from django.urls import path
from . import views

app_name = 'accesibilidad'

urlpatterns = [
    # Recursos de accesibilidad
    path('', views.IndexView.as_view(), name='index'),
    path('recursos/', views.RecursoAccesibilidadListView.as_view(), name='recurso_listar'),
    path('recursos/crear/', views.RecursoAccesibilidadCreateView.as_view(), name='recurso_crear'),
    path('recursos/<int:pk>/editar/', views.RecursoAccesibilidadUpdateView.as_view(), name='recurso_editar'),
    path('recursos/<int:pk>/eliminar/', views.RecursoAccesibilidadDeleteView.as_view(), name='recurso_eliminar'),

    # Necesidades
    path('necesidades/', views.NecesidadListView.as_view(), name='necesidad_listar'),
    path('necesidades/crear/', views.NecesidadCreateView.as_view(), name='necesidad_crear'),
    path('necesidades/<int:pk>/editar/', views.NecesidadUpdateView.as_view(), name='necesidad_editar'),
    path('necesidades/<int:pk>/eliminar/', views.NecesidadDeleteView.as_view(), name='necesidad_eliminar'),
    path('necesidades/<int:pk>/', views.NecesidadDetailView.as_view(), name='necesidad_detalle'),
]
