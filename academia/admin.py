from django.contrib import admin
from .models import (
    EstadoInscripcion, TipoActividad, TipoRecurso,
    ProgramaNivel, GrupoSeccion, CursoMateria, InscripcionCurso,
    UnidadAcademica, LeccionActividad, RecursoMaterial
)

# --- CATÁLOGOS ---
@admin.register(EstadoInscripcion)
class EstadoInscripcionAdmin(admin.ModelAdmin):
    list_display = ('nombre_estado',)

@admin.register(TipoActividad)
class TipoActividadAdmin(admin.ModelAdmin):
    list_display = ('nombre_tipo',)

@admin.register(TipoRecurso)
class TipoRecursoAdmin(admin.ModelAdmin):
    list_display = ('nombre_tipo',)

# --- TABLAS PRINCIPALES ---
@admin.register(ProgramaNivel)
class ProgramaNivelAdmin(admin.ModelAdmin):
    list_display = ('nombre_nivel', 'clave_programa', 'id_institucion')

@admin.register(GrupoSeccion)
class GrupoSeccionAdmin(admin.ModelAdmin):
    list_display = ('nombre_grupo', 'ciclo_escolar', 'grado_semestre', 'id_sede', 'id_docente_titular')
    list_filter = ('ciclo_escolar', 'id_sede')

@admin.register(CursoMateria)
class CursoMateriaAdmin(admin.ModelAdmin):
    list_display = ('nombre_materia', 'clave_materia', 'id_grupo', 'id_docente')
    search_fields = ('nombre_materia', 'clave_materia')

@admin.register(InscripcionCurso)
class InscripcionCursoAdmin(admin.ModelAdmin):
    list_display = ('id_alumno', 'id_curso', 'id_estado_inscripcion', 'progreso_porcentaje', 'fecha_inscripcion')
    list_filter = ('id_estado_inscripcion',)

@admin.register(UnidadAcademica)
class UnidadAcademicaAdmin(admin.ModelAdmin):
    list_display = ('titulo_unidad', 'numero_unidad', 'id_curso')

@admin.register(LeccionActividad)
class LeccionActividadAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'id_unidad', 'id_tipo_actividad', 'puntaje_maximo', 'estado_publicacion')
    list_filter = ('estado_publicacion', 'id_tipo_actividad')

@admin.register(RecursoMaterial)
class RecursoMaterialAdmin(admin.ModelAdmin):
    list_display = ('nombre_recurso', 'id_leccion', 'id_tipo_recurso')