from django.contrib import admin
from .models import (
    EstadoEntrega, EstadoRevision, RubricaEvaluacion, CriterioRubrica,
    EntregaTarea, ArchivoEntrega, EvaluacionIaBorrador,
    EvaluacionCriterioDetalle, BoletaCalificacion
)

# --- CATÁLOGOS ---
@admin.register(EstadoEntrega)
class EstadoEntregaAdmin(admin.ModelAdmin):
    list_display = ('nombre_estado',)

@admin.register(EstadoRevision)
class EstadoRevisionAdmin(admin.ModelAdmin):
    list_display = ('nombre_estado',)

# --- TABLAS PRINCIPALES ---
@admin.register(RubricaEvaluacion)
class RubricaEvaluacionAdmin(admin.ModelAdmin):
    list_display = ('nombre_rubrica', 'id_leccion')

@admin.register(CriterioRubrica)
class CriterioRubricaAdmin(admin.ModelAdmin):
    list_display = ('nombre_criterio', 'id_rubrica', 'puntaje_maximo')

@admin.register(EntregaTarea)
class EntregaTareaAdmin(admin.ModelAdmin):
    list_display = ('id_alumno', 'id_leccion', 'id_estado_entrega', 'id_estado_revision', 'calificacion_final', 'fecha_envio')
    list_filter = ('id_estado_entrega', 'id_estado_revision')

@admin.register(ArchivoEntrega)
class ArchivoEntregaAdmin(admin.ModelAdmin):
    list_display = ('nombre_original', 'id_entrega')

@admin.register(EvaluacionIaBorrador)
class EvaluacionIaBorradorAdmin(admin.ModelAdmin):
    list_display = ('id_entrega', 'puntaje_sugerido', 'porcentaje_confianza', 'fue_modificado_por_docente', 'puntaje_final_docente')
    list_filter = ('fue_modificado_por_docente', 'modelo_ia_utilizado')

@admin.register(EvaluacionCriterioDetalle)
class EvaluacionCriterioDetalleAdmin(admin.ModelAdmin):
    list_display = ('id_eval_ia', 'id_criterio', 'puntaje_criterio')

@admin.register(BoletaCalificacion)
class BoletaCalificacionAdmin(admin.ModelAdmin):
    list_display = ('id_inscripcion', 'parcial_1', 'parcial_2', 'parcial_3', 'promedio_final')