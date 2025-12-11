from django.contrib import admin
from .models import EquipoInventario # Importamos el modelo que definiste

# 1. Definimos una clase para personalizar la visualización en el Admin
class EquipoInventarioAdmin(admin.ModelAdmin):
    # Campos que se mostrarán en la página de listado (tabla)
    list_display = (
        'numero_inventario', 
        'descripcion', 
        'precio_adquisicion', 
        'usuario_registro'
    )
    
    # Campos que se podrán usar para buscar en el panel de administración
    search_fields = ('numero_inventario', 'descripcion')
    
    # Campos por los que se puede filtrar la lista de equipos
    list_filter = ('usuario_registro', 'precio_adquisicion')
    
    # Define los campos que aparecerán en la página de edición del objeto
    # fieldsets = (
    #     (None, {'fields': ('numero_inventario', 'descripcion')}),
    #     ('Detalles de Adquisición', {'fields': ('precio_adquisicion', 'usuario_registro')}),
    # )
    
# 2. Registramos el modelo en el sitio de administración, usando nuestra clase de personalización
admin.site.register(EquipoInventario, EquipoInventarioAdmin)