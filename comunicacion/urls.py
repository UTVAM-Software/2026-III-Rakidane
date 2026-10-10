from django.urls import path
from .views import (
    NivelRiesgoListView, NivelRiesgoDetailView, NivelRiesgoCreateView, NivelRiesgoUpdateView, NivelRiesgoDeleteView,
    EstadoValidacionAlertaListView, EstadoValidacionAlertaDetailView, EstadoValidacionAlertaCreateView, EstadoValidacionAlertaUpdateView, EstadoValidacionAlertaDeleteView,
    EstadoAsistenciaListView, EstadoAsistenciaDetailView, EstadoAsistenciaCreateView, EstadoAsistenciaUpdateView, EstadoAsistenciaDeleteView,
    PublicacionTablonListView, PublicacionTablonDetailView, PublicacionTablonCreateView, PublicacionTablonUpdateView, PublicacionTablonDeleteView,
    ComentarioTablonListView, ComentarioTablonDetailView, ComentarioTablonCreateView, ComentarioTablonUpdateView, ComentarioTablonDeleteView,
    RegistroAsistenciaListView, RegistroAsistenciaDetailView, RegistroAsistenciaCreateView, RegistroAsistenciaUpdateView, RegistroAsistenciaDeleteView,
    AlertaRiesgoIaListView, AlertaRiesgoIaDetailView, AlertaRiesgoIaCreateView, AlertaRiesgoIaUpdateView, AlertaRiesgoIaDeleteView,
    SugerenciaIaSemanalListView, SugerenciaIaSemanalDetailView, SugerenciaIaSemanalCreateView, SugerenciaIaSemanalUpdateView, SugerenciaIaSemanalDeleteView,
    LogActividadUsuarioListView, LogActividadUsuarioDetailView
)

urlpatterns = [
    # Catálogos
    path('niveles-riesgo/', NivelRiesgoListView.as_view(), name='nivelriesgo_list'),
    path('estados-validacion/', EstadoValidacionAlertaListView.as_view(), name='estadovalidacionalerta_list'),
    path('estados-asistencia/', EstadoAsistenciaListView.as_view(), name='estadoasistencia_list'),

    # PublicacionTablon
    path('publicaciones/', PublicacionTablonListView.as_view(), name='publicaciontablon_list'),
    path('publicaciones/<uuid:pk>/', PublicacionTablonDetailView.as_view(), name='publicaciontablon_detail'),
    path('publicaciones/create/', PublicacionTablonCreateView.as_view(), name='publicaciontablon_create'),
    path('publicaciones/<uuid:pk>/update/', PublicacionTablonUpdateView.as_view(), name='publicaciontablon_update'),
    path('publicaciones/<uuid:pk>/delete/', PublicacionTablonDeleteView.as_view(), name='publicaciontablon_delete'),

    # ComentarioTablon
    path('comentarios/', ComentarioTablonListView.as_view(), name='comentariotablon_list'),
    path('comentarios/<uuid:pk>/', ComentarioTablonDetailView.as_view(), name='comentariotablon_detail'),
    path('comentarios/create/', ComentarioTablonCreateView.as_view(), name='comentariotablon_create'),
    path('comentarios/<uuid:pk>/update/', ComentarioTablonUpdateView.as_view(), name='comentariotablon_update'),
    path('comentarios/<uuid:pk>/delete/', ComentarioTablonDeleteView.as_view(), name='comentariotablon_delete'),

    # RegistroAsistencia
    path('asistencias/', RegistroAsistenciaListView.as_view(), name='registroasistencia_list'),
    path('asistencias/<uuid:pk>/', RegistroAsistenciaDetailView.as_view(), name='registroasistencia_detail'),
    path('asistencias/create/', RegistroAsistenciaCreateView.as_view(), name='registroasistencia_create'),
    path('asistencias/<uuid:pk>/update/', RegistroAsistenciaUpdateView.as_view(), name='registroasistencia_update'),
    path('asistencias/<uuid:pk>/delete/', RegistroAsistenciaDeleteView.as_view(), name='registroasistencia_delete'),

    # AlertaRiesgoIa
    path('alertas-riesgo/', AlertaRiesgoIaListView.as_view(), name='alertariesgoia_list'),
    path('alertas-riesgo/<uuid:pk>/', AlertaRiesgoIaDetailView.as_view(), name='alertariesgoia_detail'),
    path('alertas-riesgo/create/', AlertaRiesgoIaCreateView.as_view(), name='alertariesgoia_create'),
    path('alertas-riesgo/<uuid:pk>/update/', AlertaRiesgoIaUpdateView.as_view(), name='alertariesgoia_update'),
    path('alertas-riesgo/<uuid:pk>/delete/', AlertaRiesgoIaDeleteView.as_view(), name='alertariesgoia_delete'),

    # SugerenciaIaSemanal
    path('sugerencias-ia/', SugerenciaIaSemanalListView.as_view(), name='sugerenciaiasemanal_list'),
    path('sugerencias-ia/<uuid:pk>/', SugerenciaIaSemanalDetailView.as_view(), name='sugerenciaiasemanal_detail'),
    path('sugerencias-ia/create/', SugerenciaIaSemanalCreateView.as_view(), name='sugerenciaiasemanal_create'),
    path('sugerencias-ia/<uuid:pk>/update/', SugerenciaIaSemanalUpdateView.as_view(), name='sugerenciaiasemanal_update'),
    path('sugerencias-ia/<uuid:pk>/delete/', SugerenciaIaSemanalDeleteView.as_view(), name='sugerenciaiasemanal_delete'),

    # LogActividadUsuario (solo lectura)
    path('logs/', LogActividadUsuarioListView.as_view(), name='logactividadusuario_list'),
    path('logs/<uuid:pk>/', LogActividadUsuarioDetailView.as_view(), name='logactividadusuario_detail'),
]