from django.contrib import admin
from mainApp.models import Categoria, Participante, Pelicula
from django.utils.html import format_html
# Register your models here.

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)

@admin.register(Participante)
class ParticipanteAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'recomendado_por', 'calificacion','vista_imagen')
    list_filter = ('categoria', 'recomendado_por')
    search_fields = ('titulo', 'sinopsis')
    ordering = ('titulo',) 
    def vista_imagen(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" width="100" height="100" />', obj.imagen.url)
        return "No Image"
