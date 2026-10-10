from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import (
    EstadoEntrega, EstadoRevision, RubricaEvaluacion, CriterioRubrica,
    EntregaTarea, ArchivoEntrega, EvaluacionIaBorrador,
    EvaluacionCriterioDetalle, BoletaCalificacion
)

# --- ESTADO ENTREGA ---
class EstadoEntregaListView(ListView):
    model = EstadoEntrega

class EstadoEntregaDetailView(DetailView):
    model = EstadoEntrega

class EstadoEntregaCreateView(CreateView):
    model = EstadoEntrega
    fields = ['nombre_estado']
    template_name = 'evaluacion/nuevo_estado_entrega.html'
    success_url = '/evaluacion/estados-entrega/'

class EstadoEntregaUpdateView(UpdateView):
    model = EstadoEntrega
    fields = ['nombre_estado']
    template_name = 'evaluacion/editar_estado_entrega.html'
    success_url = '/evaluacion/estados-entrega/'

class EstadoEntregaDeleteView(DeleteView):
    model = EstadoEntrega
    success_url = '/evaluacion/estados-entrega/'


# --- ESTADO REVISION ---
class EstadoRevisionListView(ListView):
    model = EstadoRevision

class EstadoRevisionDetailView(DetailView):
    model = EstadoRevision

class EstadoRevisionCreateView(CreateView):
    model = EstadoRevision
    fields = ['nombre_estado']
    template_name = 'evaluacion/nuevo_estado_revision.html'
    success_url = '/evaluacion/estados-revision/'

class EstadoRevisionUpdateView(UpdateView):
    model = EstadoRevision
    fields = ['nombre_estado']
    template_name = 'evaluacion/editar_estado_revision.html'
    success_url = '/evaluacion/estados-revision/'

class EstadoRevisionDeleteView(DeleteView):
    model = EstadoRevision
    success_url = '/evaluacion/estados-revision/'


# --- RUBRICA EVALUACION ---
class RubricaEvaluacionListView(ListView):
    model = RubricaEvaluacion

class RubricaEvaluacionDetailView(DetailView):
    model = RubricaEvaluacion

class RubricaEvaluacionCreateView(CreateView):
    model = RubricaEvaluacion
    fields = ['id_leccion', 'nombre_rubrica', 'descripcion_general']
    template_name = 'evaluacion/nuevo_rubrica.html'
    success_url = '/evaluacion/rubricas/'

class RubricaEvaluacionUpdateView(UpdateView):
    model = RubricaEvaluacion
    fields = ['id_leccion', 'nombre_rubrica', 'descripcion_general']
    template_name = 'evaluacion/editar_rubrica.html'
    success_url = '/evaluacion/rubricas/'

class RubricaEvaluacionDeleteView(DeleteView):
    model = RubricaEvaluacion
    success_url = '/evaluacion/rubricas/'


# --- CRITERIO RUBRICA ---
class CriterioRubricaListView(ListView):
    model = CriterioRubrica

class CriterioRubricaDetailView(DetailView):
    model = CriterioRubrica

class CriterioRubricaCreateView(CreateView):
    model = CriterioRubrica
    fields = ['id_rubrica', 'nombre_criterio', 'descripcion_criterio', 'puntaje_maximo']
    template_name = 'evaluacion/nuevo_criterio.html'
    success_url = '/evaluacion/criterios/'

class CriterioRubricaUpdateView(UpdateView):
    model = CriterioRubrica
    fields = ['id_rubrica', 'nombre_criterio', 'descripcion_criterio', 'puntaje_maximo']
    template_name = 'evaluacion/editar_criterio.html'
    success_url = '/evaluacion/criterios/'

class CriterioRubricaDeleteView(DeleteView):
    model = CriterioRubrica
    success_url = '/evaluacion/criterios/'


# --- ENTREGA TAREA ---
class EntregaTareaListView(ListView):
    model = EntregaTarea

class EntregaTareaDetailView(DetailView):
    model = EntregaTarea

class EntregaTareaCreateView(CreateView):
    model = EntregaTarea
    fields = ['id_leccion', 'id_alumno', 'id_estado_entrega', 'id_estado_revision', 'texto_contenido', 'calificacion_final', 'retroalimentacion_docente']
    template_name = 'evaluacion/nuevo_entrega.html'
    success_url = '/evaluacion/entregas/'

class EntregaTareaUpdateView(UpdateView):
    model = EntregaTarea
    fields = ['id_estado_entrega', 'id_estado_revision', 'texto_contenido', 'calificacion_final', 'retroalimentacion_docente']
    template_name = 'evaluacion/editar_entrega.html'
    success_url = '/evaluacion/entregas/'

class EntregaTareaDeleteView(DeleteView):
    model = EntregaTarea
    success_url = '/evaluacion/entregas/'


# --- ARCHIVO ENTREGA ---
class ArchivoEntregaListView(ListView):
    model = ArchivoEntrega

class ArchivoEntregaDetailView(DetailView):
    model = ArchivoEntrega

class ArchivoEntregaCreateView(CreateView):
    model = ArchivoEntrega
    fields = ['id_entrega', 'nombre_original', 'ruta_almacenamiento']
    template_name = 'evaluacion/nuevo_archivo_entrega.html'
    success_url = '/evaluacion/archivos-entrega/'

class ArchivoEntregaUpdateView(UpdateView):
    model = ArchivoEntrega
    fields = ['nombre_original', 'ruta_almacenamiento']
    template_name = 'evaluacion/editar_archivo_entrega.html'
    success_url = '/evaluacion/archivos-entrega/'

class ArchivoEntregaDeleteView(DeleteView):
    model = ArchivoEntrega
    success_url = '/evaluacion/archivos-entrega/'


# --- EVALUACION IA BORRADOR ---
class EvaluacionIaBorradorListView(ListView):
    model = EvaluacionIaBorrador

class EvaluacionIaBorradorDetailView(DetailView):
    model = EvaluacionIaBorrador

class EvaluacionIaBorradorCreateView(CreateView):
    model = EvaluacionIaBorrador
    fields = [
        'id_entrega', 'modelo_ia_utilizado', 'puntaje_sugerido', 'porcentaje_confianza',
        'comentario_general', 'prompt_utilizado', 'datos_origen_json',
        'fue_modificado_por_docente', 'puntaje_final_docente'
    ]
    template_name = 'evaluacion/nuevo_eval_ia.html'
    success_url = '/evaluacion/evaluaciones-ia/'

class EvaluacionIaBorradorUpdateView(UpdateView):
    model = EvaluacionIaBorrador
    fields = [
        'modelo_ia_utilizado', 'puntaje_sugerido', 'porcentaje_confianza',
        'comentario_general', 'prompt_utilizado', 'datos_origen_json',
        'fue_modificado_por_docente', 'puntaje_final_docente'
    ]
    template_name = 'evaluacion/editar_eval_ia.html'
    success_url = '/evaluacion/evaluaciones-ia/'

class EvaluacionIaBorradorDeleteView(DeleteView):
    model = EvaluacionIaBorrador
    success_url = '/evaluacion/evaluaciones-ia/'


# --- EVALUACION CRITERIO DETALLE ---
class EvaluacionCriterioDetalleListView(ListView):
    model = EvaluacionCriterioDetalle

class EvaluacionCriterioDetalleDetailView(DetailView):
    model = EvaluacionCriterioDetalle

class EvaluacionCriterioDetalleCreateView(CreateView):
    model = EvaluacionCriterioDetalle
    fields = ['id_eval_ia', 'id_criterio', 'puntaje_criterio', 'evidencia_citada']
    template_name = 'evaluacion/nuevo_eval_criterio.html'
    success_url = '/evaluacion/detalles-criterio/'

class EvaluacionCriterioDetalleUpdateView(UpdateView):
    model = EvaluacionCriterioDetalle
    fields = ['puntaje_criterio', 'evidencia_citada']
    template_name = 'evaluacion/editar_eval_criterio.html'
    success_url = '/evaluacion/detalles-criterio/'

class EvaluacionCriterioDetalleDeleteView(DeleteView):
    model = EvaluacionCriterioDetalle
    success_url = '/evaluacion/detalles-criterio/'


# --- BOLETA CALIFICACION ---
class BoletaCalificacionListView(ListView):
    model = BoletaCalificacion

class BoletaCalificacionDetailView(DetailView):
    model = BoletaCalificacion

class BoletaCalificacionCreateView(CreateView):
    model = BoletaCalificacion
    fields = ['id_inscripcion', 'parcial_1', 'parcial_2', 'parcial_3', 'promedio_final', 'observaciones']
    template_name = 'evaluacion/nuevo_boleta.html'
    success_url = '/evaluacion/boletas/'

class BoletaCalificacionUpdateView(UpdateView):
    model = BoletaCalificacion
    fields = ['parcial_1', 'parcial_2', 'parcial_3', 'promedio_final', 'observaciones']
    template_name = 'evaluacion/editar_boleta.html'
    success_url = '/evaluacion/boletas/'

class BoletaCalificacionDeleteView(DeleteView):
    model = BoletaCalificacion
    success_url = '/evaluacion/boletas/'