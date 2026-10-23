from django.urls import path
from django.contrib.auth.decorators import permission_required, login_required
from .views import (
    EstadoEntregaListView, EstadoEntregaDetailView, EstadoEntregaCreateView, EstadoEntregaUpdateView, EstadoEntregaDeleteView,
    EstadoRevisionListView, EstadoRevisionDetailView, EstadoRevisionCreateView, EstadoRevisionUpdateView, EstadoRevisionDeleteView,
    RubricaEvaluacionListView, RubricaEvaluacionDetailView, RubricaEvaluacionCreateView, RubricaEvaluacionUpdateView, RubricaEvaluacionDeleteView,
    CriterioRubricaListView, CriterioRubricaDetailView, CriterioRubricaCreateView, CriterioRubricaUpdateView, CriterioRubricaDeleteView,
    EntregaTareaListView, EntregaTareaDetailView, EntregaTareaCreateView, EntregaTareaUpdateView, EntregaTareaDeleteView,
    ArchivoEntregaListView, ArchivoEntregaDetailView, ArchivoEntregaCreateView, ArchivoEntregaUpdateView, ArchivoEntregaDeleteView,
    EvaluacionIaBorradorListView, EvaluacionIaBorradorDetailView, EvaluacionIaBorradorCreateView, EvaluacionIaBorradorUpdateView, EvaluacionIaBorradorDeleteView,
    EvaluacionCriterioDetalleListView, EvaluacionCriterioDetalleDetailView, EvaluacionCriterioDetalleCreateView, EvaluacionCriterioDetalleUpdateView, EvaluacionCriterioDetalleDeleteView,
    BoletaCalificacionListView, BoletaCalificacionDetailView, BoletaCalificacionCreateView, BoletaCalificacionUpdateView, BoletaCalificacionDeleteView,
)

urlpatterns = [
    # Ruta principal para /evaluacion/
    path('', login_required(RubricaEvaluacionListView.as_view()), name='evaluacion_index'),

    # --- CATÁLOGOS ---
    path('estados-entrega/', login_required(EstadoEntregaListView.as_view()), name='estadoentrega_list'),
    path('estados-revision/', login_required(EstadoRevisionListView.as_view()), name='estadorevision_list'),

    # --- RÚBRICA EVALUACIÓN ---
    path('rubricas/', login_required(RubricaEvaluacionListView.as_view()), name='rubricaevaluacion_list'),
    path('rubricas/<uuid:pk>/', login_required(RubricaEvaluacionDetailView.as_view()), name='rubricaevaluacion_detail'),
    path('rubricas/create/', permission_required('evaluacion.add_rubricaevaluacion')(RubricaEvaluacionCreateView.as_view()), name='rubricaevaluacion_create'),
    path('rubricas/<uuid:pk>/update/', permission_required('evaluacion.change_rubricaevaluacion')(RubricaEvaluacionUpdateView.as_view()), name='rubricaevaluacion_update'),
    path('rubricas/<uuid:pk>/delete/', permission_required('evaluacion.delete_rubricaevaluacion')(RubricaEvaluacionDeleteView.as_view()), name='rubricaevaluacion_delete'),

    # --- CRITERIO RÚBRICA ---
    path('criterios/', login_required(CriterioRubricaListView.as_view()), name='criteriorubrica_list'),
    path('criterios/<uuid:pk>/', login_required(CriterioRubricaDetailView.as_view()), name='criteriorubrica_detail'),
    path('criterios/create/', permission_required('evaluacion.add_criteriorubrica')(CriterioRubricaCreateView.as_view()), name='criteriorubrica_create'),
    path('criterios/<uuid:pk>/update/', permission_required('evaluacion.change_criteriorubrica')(CriterioRubricaUpdateView.as_view()), name='criteriorubrica_update'),
    path('criterios/<uuid:pk>/delete/', permission_required('evaluacion.delete_criteriorubrica')(CriterioRubricaDeleteView.as_view()), name='criteriorubrica_delete'),

    # --- ENTREGA TAREA ---
    path('entregas/', login_required(EntregaTareaListView.as_view()), name='entregatarea_list'),
    path('entregas/<uuid:pk>/', login_required(EntregaTareaDetailView.as_view()), name='entregatarea_detail'),
    path('entregas/create/', permission_required('evaluacion.add_entregatarea')(EntregaTareaCreateView.as_view()), name='entregatarea_create'),
    path('entregas/<uuid:pk>/update/', permission_required('evaluacion.change_entregatarea')(EntregaTareaUpdateView.as_view()), name='entregatarea_update'),
    path('entregas/<uuid:pk>/delete/', permission_required('evaluacion.delete_entregatarea')(EntregaTareaDeleteView.as_view()), name='entregatarea_delete'),

    # --- ARCHIVO ENTREGA ---
    path('archivos-entrega/', login_required(ArchivoEntregaListView.as_view()), name='archivoentrega_list'),
    path('archivos-entrega/<uuid:pk>/', login_required(ArchivoEntregaDetailView.as_view()), name='archivoentrega_detail'),
    path('archivos-entrega/create/', permission_required('evaluacion.add_archivoentrega')(ArchivoEntregaCreateView.as_view()), name='archivoentrega_create'),
    path('archivos-entrega/<uuid:pk>/update/', permission_required('evaluacion.change_archivoentrega')(ArchivoEntregaUpdateView.as_view()), name='archivoentrega_update'),
    path('archivos-entrega/<uuid:pk>/delete/', permission_required('evaluacion.delete_archivoentrega')(ArchivoEntregaDeleteView.as_view()), name='archivoentrega_delete'),

    # --- EVALUACIÓN IA BORRADOR ---
    path('evaluaciones-ia/', login_required(EvaluacionIaBorradorListView.as_view()), name='evaluacioniaborrador_list'),
    path('evaluaciones-ia/<uuid:pk>/', login_required(EvaluacionIaBorradorDetailView.as_view()), name='evaluacioniaborrador_detail'),
    path('evaluaciones-ia/create/', permission_required('evaluacion.add_evaluacioniaborrador')(EvaluacionIaBorradorCreateView.as_view()), name='evaluacioniaborrador_create'),
    path('evaluaciones-ia/<uuid:pk>/update/', permission_required('evaluacion.change_evaluacioniaborrador')(EvaluacionIaBorradorUpdateView.as_view()), name='evaluacioniaborrador_update'),
    path('evaluaciones-ia/<uuid:pk>/delete/', permission_required('evaluacion.delete_evaluacioniaborrador')(EvaluacionIaBorradorDeleteView.as_view()), name='evaluacioniaborrador_delete'),

    # --- EVALUACIÓN CRITERIO DETALLE ---
    path('detalles-criterio/', login_required(EvaluacionCriterioDetalleListView.as_view()), name='evaluacioncriteriodetalle_list'),
    path('detalles-criterio/<uuid:pk>/', login_required(EvaluacionCriterioDetalleDetailView.as_view()), name='evaluacioncriteriodetalle_detail'),
    path('detalles-criterio/create/', permission_required('evaluacion.add_evaluacioncriteriodetalle')(EvaluacionCriterioDetalleCreateView.as_view()), name='evaluacioncriteriodetalle_create'),
    path('detalles-criterio/<uuid:pk>/update/', permission_required('evaluacion.change_evaluacioncriteriodetalle')(EvaluacionCriterioDetalleUpdateView.as_view()), name='evaluacioncriteriodetalle_update'),
    path('detalles-criterio/<uuid:pk>/delete/', permission_required('evaluacion.delete_evaluacioncriteriodetalle')(EvaluacionCriterioDetalleDeleteView.as_view()), name='evaluacioncriteriodetalle_delete'),

    # --- BOLETA CALIFICACIÓN ---
    path('boletas/', login_required(BoletaCalificacionListView.as_view()), name='boletacalificacion_list'),
    path('boletas/<uuid:pk>/', login_required(BoletaCalificacionDetailView.as_view()), name='boletacalificacion_detail'),
    path('boletas/create/', permission_required('evaluacion.add_boletacalificacion')(BoletaCalificacionCreateView.as_view()), name='boletacalificacion_create'),
    path('boletas/<uuid:pk>/update/', permission_required('evaluacion.change_boletacalificacion')(BoletaCalificacionUpdateView.as_view()), name='boletacalificacion_update'),
    path('boletas/<uuid:pk>/delete/', permission_required('evaluacion.delete_boletacalificacion')(BoletaCalificacionDeleteView.as_view()), name='boletacalificacion_delete'),
]