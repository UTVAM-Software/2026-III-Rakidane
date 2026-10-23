from django.urls import path
from django.contrib.auth.decorators import permission_required, login_required
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
    # --- CATÁLOGOS ---
    path('niveles-riesgo/', login_required(NivelRiesgoListView.as_view()), name='nivelriesgo_list'),
    path('estados-validacion/', login_required(EstadoValidacionAlertaListView.as_view()), name='estadovalidacionalerta_list'),
    path('estados-asistencia/', login_required(EstadoAsistenciaListView.as_view()), name='estadoasistencia_list'),

    # --- PUBLICACIÓN TABLÓN ---
    path('publicaciones/', login_required(PublicacionTablonListView.as_view()), name='publicaciontablon_list'),
    path('publicaciones/<uuid:pk>/', login_required(PublicacionTablonDetailView.as_view()), name='publicaciontablon_detail'),
    path('publicaciones/create/', permission_required('comunicacion.add_publicaciontablon')(PublicacionTablonCreateView.as_view()), name='publicaciontablon_create'),
    path('publicaciones/<uuid:pk>/update/', permission_required('comunicacion.change_publicaciontablon')(PublicacionTablonUpdateView.as_view()), name='publicaciontablon_update'),
    path('publicaciones/<uuid:pk>/delete/', permission_required('comunicacion.delete_publicaciontablon')(PublicacionTablonDeleteView.as_view()), name='publicaciontablon_delete'),

    # --- COMENTARIO TABLÓN ---
    path('comentarios/', login_required(ComentarioTablonListView.as_view()), name='comentariotablon_list'),
    path('comentarios/<uuid:pk>/', login_required(ComentarioTablonDetailView.as_view()), name='comentariotablon_detail'),
    path('comentarios/create/', permission_required('comunicacion.add_comentariotablon')(ComentarioTablonCreateView.as_view()), name='comentariotablon_create'),
    path('comentarios/<uuid:pk>/update/', permission_required('comunicacion.change_comentariotablon')(ComentarioTablonUpdateView.as_view()), name='comentariotablon_update'),
    path('comentarios/<uuid:pk>/delete/', permission_required('comunicacion.delete_comentariotablon')(ComentarioTablonDeleteView.as_view()), name='comentariotablon_delete'),

    # --- REGISTRO ASISTENCIA ---
    path('asistencias/', login_required(RegistroAsistenciaListView.as_view()), name='registroasistencia_list'),
    path('asistencias/<uuid:pk>/', login_required(RegistroAsistenciaDetailView.as_view()), name='registroasistencia_detail'),
    path('asistencias/create/', permission_required('comunicacion.add_registroasistencia')(RegistroAsistenciaCreateView.as_view()), name='registroasistencia_create'),
    path('asistencias/<uuid:pk>/update/', permission_required('comunicacion.change_registroasistencia')(RegistroAsistenciaUpdateView.as_view()), name='registroasistencia_update'),
    path('asistencias/<uuid:pk>/delete/', permission_required('comunicacion.delete_registroasistencia')(RegistroAsistenciaDeleteView.as_view()), name='registroasistencia_delete'),

    # --- ALERTA RIESGO IA ---
    path('alertas-riesgo/', login_required(AlertaRiesgoIaListView.as_view()), name='alertariesgoia_list'),
    path('alertas-riesgo/<uuid:pk>/', login_required(AlertaRiesgoIaDetailView.as_view()), name='alertariesgoia_detail'),
    path('alertas-riesgo/create/', permission_required('comunicacion.add_alertariesgoia')(AlertaRiesgoIaCreateView.as_view()), name='alertariesgoia_create'),
    path('alertas-riesgo/<uuid:pk>/update/', permission_required('comunicacion.change_alertariesgoia')(AlertaRiesgoIaUpdateView.as_view()), name='alertariesgoia_update'),
    path('alertas-riesgo/<uuid:pk>/delete/', permission_required('comunicacion.delete_alertariesgoia')(AlertaRiesgoIaDeleteView.as_view()), name='alertariesgoia_delete'),

    # --- SUGERENCIA IA SEMANAL ---
    path('sugerencias-ia/', login_required(SugerenciaIaSemanalListView.as_view()), name='sugerenciaiasemanal_list'),
    path('sugerencias-ia/<uuid:pk>/', login_required(SugerenciaIaSemanalDetailView.as_view()), name='sugerenciaiasemanal_detail'),
    path('sugerencias-ia/create/', permission_required('comunicacion.add_sugerenciaiasemanal')(SugerenciaIaSemanalCreateView.as_view()), name='sugerenciaiasemanal_create'),
    path('sugerencias-ia/<uuid:pk>/update/', permission_required('comunicacion.change_sugerenciaiasemanal')(SugerenciaIaSemanalUpdateView.as_view()), name='sugerenciaiasemanal_update'),
    path('sugerencias-ia/<uuid:pk>/delete/', permission_required('comunicacion.delete_sugerenciaiasemanal')(SugerenciaIaSemanalDeleteView.as_view()), name='sugerenciaiasemanal_delete'),

    # --- LOG ACTIVIDAD USUARIO (Solo Lectura con protección de sesión) ---
    path('logs/', login_required(LogActividadUsuarioListView.as_view()), name='logactividadusuario_list'),
    path('logs/<uuid:pk>/', login_required(LogActividadUsuarioDetailView.as_view()), name='logactividadusuario_detail'),
]