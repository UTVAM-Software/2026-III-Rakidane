from django.contrib import admin
from .models import (
    NivelRiesgo, EstadoValidacionAlerta, EstadoAsistencia,
    PublicacionTablon, ComentarioTablon, RegistroAsistencia,
    AlertaRiesgoIa, SugerenciaIaSemanal, LogActividadUsuario
)

# --- CATÁLOGOS ---
@admin.register(NivelRiesgo)
class NivelRiesgoAdmin(admin.ModelAdmin):
    list_display = ('nombre_nivel', 'codigo_color_hex', 'descripcion')

@admin.register(EstadoValidacionAlerta)
class EstadoValidacionAlertaAdmin(admin.ModelAdmin):
    list_display = ('nombre_estado',)

@admin.register(EstadoAsistencia)
class EstadoAsistenciaAdmin(admin.ModelAdmin):
    list_display = ('nombre_estado',)

# --- TABLAS PRINCIPALES ---
@admin.register(PublicacionTablon)
class PublicacionTablonAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'id_curso', 'id_autor', 'fijado_inicio', 'creado_en')

@admin.register(ComentarioTablon)
class ComentarioTablonAdmin(admin.ModelAdmin):
    list_display = ('id_publicacion', 'id_cuenta', 'creado_en')

@admin.register(RegistroAsistencia)
class RegistroAsistenciaAdmin(admin.ModelAdmin):
    list_display = ('id_alumno', 'id_curso', 'fecha_registro', 'id_estado_asistencia')
    list_filter = ('id_estado_asistencia', 'fecha_registro')

@admin.register(AlertaRiesgoIa)
class AlertaRiesgoIaAdmin(admin.ModelAdmin):
    list_display = ('id_alumno', 'id_nivel_riesgo', 'id_estado_validacion', 'creado_en')
    list_filter = ('id_nivel_riesgo', 'id_estado_validacion')

@admin.register(SugerenciaIaSemanal)
class SugerenciaIaSemanalAdmin(admin.ModelAdmin):
    list_display = ('id_cuenta', 'creado_en')

@admin.register(LogActividadUsuario)
class LogActividadUsuarioAdmin(admin.ModelAdmin):
    list_display = ('id_cuenta', 'ip_origen', 'accion_realizada', 'creado_en')
    list_filter = ('creado_en',)