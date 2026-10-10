from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import (
    NivelRiesgo, EstadoValidacionAlerta, EstadoAsistencia,
    PublicacionTablon, ComentarioTablon, RegistroAsistencia,
    AlertaRiesgoIa, SugerenciaIaSemanal, LogActividadUsuario
)

# --- NIVEL RIESGO ---
class NivelRiesgoListView(ListView):
    model = NivelRiesgo

class NivelRiesgoDetailView(DetailView):
    model = NivelRiesgo

class NivelRiesgoCreateView(CreateView):
    model = NivelRiesgo
    fields = ['nombre_nivel', 'codigo_color_hex', 'descripcion']
    template_name = 'comunicacion/nuevo_nivel_riesgo.html'
    success_url = '/comunicacion/niveles-riesgo/'

class NivelRiesgoUpdateView(UpdateView):
    model = NivelRiesgo
    fields = ['nombre_nivel', 'codigo_color_hex', 'descripcion']
    template_name = 'comunicacion/editar_nivel_riesgo.html'
    success_url = '/comunicacion/niveles-riesgo/'

class NivelRiesgoDeleteView(DeleteView):
    model = NivelRiesgo
    success_url = '/comunicacion/niveles-riesgo/'


# --- ESTADO VALIDACION ALERTA ---
class EstadoValidacionAlertaListView(ListView):
    model = EstadoValidacionAlerta

class EstadoValidacionAlertaDetailView(DetailView):
    model = EstadoValidacionAlerta

class EstadoValidacionAlertaCreateView(CreateView):
    model = EstadoValidacionAlerta
    fields = ['nombre_estado']
    template_name = 'comunicacion/nuevo_estado_validacion.html'
    success_url = '/comunicacion/estados-validacion/'

class EstadoValidacionAlertaUpdateView(UpdateView):
    model = EstadoValidacionAlerta
    fields = ['nombre_estado']
    template_name = 'comunicacion/editar_estado_validacion.html'
    success_url = '/comunicacion/estados-validacion/'

class EstadoValidacionAlertaDeleteView(DeleteView):
    model = EstadoValidacionAlerta
    success_url = '/comunicacion/estados-validacion/'


# --- ESTADO ASISTENCIA ---
class EstadoAsistenciaListView(ListView):
    model = EstadoAsistencia

class EstadoAsistenciaDetailView(DetailView):
    model = EstadoAsistencia

class EstadoAsistenciaCreateView(CreateView):
    model = EstadoAsistencia
    fields = ['nombre_estado']
    template_name = 'comunicacion/nuevo_estado_asistencia.html'
    success_url = '/comunicacion/estados-asistencia/'

class EstadoAsistenciaUpdateView(UpdateView):
    model = EstadoAsistencia
    fields = ['nombre_estado']
    template_name = 'comunicacion/editar_estado_asistencia.html'
    success_url = '/comunicacion/estados-asistencia/'

class EstadoAsistenciaDeleteView(DeleteView):
    model = EstadoAsistencia
    success_url = '/comunicacion/estados-asistencia/'


# --- PUBLICACION TABLON ---
class PublicacionTablonListView(ListView):
    model = PublicacionTablon

class PublicacionTablonDetailView(DetailView):
    model = PublicacionTablon

class PublicacionTablonCreateView(CreateView):
    model = PublicacionTablon
    fields = ['id_curso', 'id_autor', 'titulo', 'contenido_texto', 'fijado_inicio']
    template_name = 'comunicacion/nuevo_publicacion_tablon.html'
    success_url = '/comunicacion/publicaciones/'

class PublicacionTablonUpdateView(UpdateView):
    model = PublicacionTablon
    fields = ['titulo', 'contenido_texto', 'fijado_inicio']
    template_name = 'comunicacion/editar_publicacion_tablon.html'
    success_url = '/comunicacion/publicaciones/'

class PublicacionTablonDeleteView(DeleteView):
    model = PublicacionTablon
    success_url = '/comunicacion/publicaciones/'


# --- COMENTARIO TABLON ---
class ComentarioTablonListView(ListView):
    model = ComentarioTablon

class ComentarioTablonDetailView(DetailView):
    model = ComentarioTablon

class ComentarioTablonCreateView(CreateView):
    model = ComentarioTablon
    fields = ['id_publicacion', 'id_cuenta', 'mensaje']
    template_name = 'comunicacion/nuevo_comentario_tablon.html'
    success_url = '/comunicacion/comentarios/'

class ComentarioTablonUpdateView(UpdateView):
    model = ComentarioTablon
    fields = ['mensaje']
    template_name = 'comunicacion/editar_comentario_tablon.html'
    success_url = '/comunicacion/comentarios/'

class ComentarioTablonDeleteView(DeleteView):
    model = ComentarioTablon
    success_url = '/comunicacion/comentarios/'


# --- REGISTRO ASISTENCIA ---
class RegistroAsistenciaListView(ListView):
    model = RegistroAsistencia

class RegistroAsistenciaDetailView(DetailView):
    model = RegistroAsistencia

class RegistroAsistenciaCreateView(CreateView):
    model = RegistroAsistencia
    fields = ['id_alumno', 'id_curso', 'id_estado_asistencia', 'fecha_registro', 'justificacion_observacion']
    template_name = 'comunicacion/nuevo_registro_asistencia.html'
    success_url = '/comunicacion/asistencias/'

class RegistroAsistenciaUpdateView(UpdateView):
    model = RegistroAsistencia
    fields = ['id_estado_asistencia', 'fecha_registro', 'justificacion_observacion']
    template_name = 'comunicacion/editar_registro_asistencia.html'
    success_url = '/comunicacion/asistencias/'

class RegistroAsistenciaDeleteView(DeleteView):
    model = RegistroAsistencia
    success_url = '/comunicacion/asistencias/'


# --- ALERTA RIESGO IA ---
class AlertaRiesgoIaListView(ListView):
    model = AlertaRiesgoIa

class AlertaRiesgoIaDetailView(DetailView):
    model = AlertaRiesgoIa

class AlertaRiesgoIaCreateView(CreateView):
    model = AlertaRiesgoIa
    fields = ['id_alumno', 'id_nivel_riesgo', 'id_estado_validacion', 'motivo_alerta', 'metricas_disparadoras']
    template_name = 'comunicacion/nuevo_alerta_riesgo.html'
    success_url = '/comunicacion/alertas-riesgo/'

class AlertaRiesgoIaUpdateView(UpdateView):
    model = AlertaRiesgoIa
    fields = ['id_nivel_riesgo', 'id_estado_validacion', 'motivo_alerta', 'metricas_disparadoras']
    template_name = 'comunicacion/editar_alerta_riesgo.html'
    success_url = '/comunicacion/alertas-riesgo/'

class AlertaRiesgoIaDeleteView(DeleteView):
    model = AlertaRiesgoIa
    success_url = '/comunicacion/alertas-riesgo/'


# --- SUGERENCIA IA SEMANAL ---
class SugerenciaIaSemanalListView(ListView):
    model = SugerenciaIaSemanal

class SugerenciaIaSemanalDetailView(DetailView):
    model = SugerenciaIaSemanal

class SugerenciaIaSemanalCreateView(CreateView):
    model = SugerenciaIaSemanal
    fields = ['id_cuenta', 'mensaje_accionable']
    template_name = 'comunicacion/nuevo_sugerencia_ia.html'
    success_url = '/comunicacion/sugerencias-ia/'

class SugerenciaIaSemanalUpdateView(UpdateView):
    model = SugerenciaIaSemanal
    fields = ['mensaje_accionable']
    template_name = 'comunicacion/editar_sugerencia_ia.html'
    success_url = '/comunicacion/sugerencias-ia/'

class SugerenciaIaSemanalDeleteView(DeleteView):
    model = SugerenciaIaSemanal
    success_url = '/comunicacion/sugerencias-ia/'


# --- LOG ACTIVIDAD USUARIO ---
class LogActividadUsuarioListView(ListView):
    model = LogActividadUsuario

class LogActividadUsuarioDetailView(DetailView):
    model = LogActividadUsuario