from django.contrib import admin
from .models import Proyecto

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'tecnologias', 'fecha_creacion', 'destacado']
    list_filter = ['destacado', 'fecha_creacion']
    search_fields = ['titulo', 'tecnologias', 'descripcion']
