from django.urls import path
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
    # Catálogos
    path('estados-entrega/', EstadoEntregaListView.as_view(), name='estadoentrega_list'),
    path('estados-revision/', EstadoRevisionListView.as_view(), name='estadorevision_list'),

    # RubricaEvaluacion
    path('rubricas/', RubricaEvaluacionListView.as_view(), name='rubricaevaluacion_list'),
    path('rubricas/<uuid:pk>/', RubricaEvaluacionDetailView.as_view(), name='rubricaevaluacion_detail'),
    path('rubricas/create/', RubricaEvaluacionCreateView.as_view(), name='rubricaevaluacion_create'),
    path('rubricas/<uuid:pk>/update/', RubricaEvaluacionUpdateView.as_view(), name='rubricaevaluacion_update'),
    path('rubricas/<uuid:pk>/delete/', RubricaEvaluacionDeleteView.as_view(), name='rubricaevaluacion_delete'),

    # CriterioRubrica
    path('criterios/', CriterioRubricaListView.as_view(), name='criteriorubrica_list'),
    path('criterios/<uuid:pk>/', CriterioRubricaDetailView.as_view(), name='criteriorubrica_detail'),
    path('criterios/create/', CriterioRubricaCreateView.as_view(), name='criteriorubrica_create'),
    path('criterios/<uuid:pk>/update/', CriterioRubricaUpdateView.as_view(), name='criteriorubrica_update'),
    path('criterios/<uuid:pk>/delete/', CriterioRubricaDeleteView.as_view(), name='criteriorubrica_delete'),

    # EntregaTarea
    path('entregas/', EntregaTareaListView.as_view(), name='entregatarea_list'),
    path('entregas/<uuid:pk>/', EntregaTareaDetailView.as_view(), name='entregatarea_detail'),
    path('entregas/create/', EntregaTareaCreateView.as_view(), name='entregatarea_create'),
    path('entregas/<uuid:pk>/update/', EntregaTareaUpdateView.as_view(), name='entregatarea_update'),
    path('entregas/<uuid:pk>/delete/', EntregaTareaDeleteView.as_view(), name='entregatarea_delete'),

    # ArchivoEntrega
    path('archivos-entrega/', ArchivoEntregaListView.as_view(), name='archivoentrega_list'),
    path('archivos-entrega/<uuid:pk>/', ArchivoEntregaDetailView.as_view(), name='archivoentrega_detail'),
    path('archivos-entrega/create/', ArchivoEntregaCreateView.as_view(), name='archivoentrega_create'),
    path('archivos-entrega/<uuid:pk>/update/', ArchivoEntregaUpdateView.as_view(), name='archivoentrega_update'),
    path('archivos-entrega/<uuid:pk>/delete/', ArchivoEntregaDeleteView.as_view(), name='archivoentrega_delete'),

    # EvaluacionIaBorrador
    path('evaluaciones-ia/', EvaluacionIaBorradorListView.as_view(), name='evaluacioniaborrador_list'),
    path('evaluaciones-ia/<uuid:pk>/', EvaluacionIaBorradorDetailView.as_view(), name='evaluacioniaborrador_detail'),
    path('evaluaciones-ia/create/', EvaluacionIaBorradorCreateView.as_view(), name='evaluacioniaborrador_create'),
    path('evaluaciones-ia/<uuid:pk>/update/', EvaluacionIaBorradorUpdateView.as_view(), name='evaluacioniaborrador_update'),
    path('evaluaciones-ia/<uuid:pk>/delete/', EvaluacionIaBorradorDeleteView.as_view(), name='evaluacioniaborrador_delete'),

    # EvaluacionCriterioDetalle
    path('detalles-criterio/', EvaluacionCriterioDetalleListView.as_view(), name='evaluacioncriteriodetalle_list'),
    path('detalles-criterio/<uuid:pk>/', EvaluacionCriterioDetalleDetailView.as_view(), name='evaluacioncriteriodetalle_detail'),
    path('detalles-criterio/create/', EvaluacionCriterioDetalleCreateView.as_view(), name='evaluacioncriteriodetalle_create'),
    path('detalles-criterio/<uuid:pk>/update/', EvaluacionCriterioDetalleUpdateView.as_view(), name='evaluacioncriteriodetalle_update'),
    path('detalles-criterio/<uuid:pk>/delete/', EvaluacionCriterioDetalleDeleteView.as_view(), name='evaluacioncriteriodetalle_delete'),

    # BoletaCalificacion
    path('boletas/', BoletaCalificacionListView.as_view(), name='boletacalificacion_list'),
    path('boletas/<uuid:pk>/', BoletaCalificacionDetailView.as_view(), name='boletacalificacion_detail'),
    path('boletas/create/', BoletaCalificacionCreateView.as_view(), name='boletacalificacion_create'),
    path('boletas/<uuid:pk>/update/', BoletaCalificacionUpdateView.as_view(), name='boletacalificacion_update'),
    path('boletas/<uuid:pk>/delete/', BoletaCalificacionDeleteView.as_view(), name='boletacalificacion_delete'),
]