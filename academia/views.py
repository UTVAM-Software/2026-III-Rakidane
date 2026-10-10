from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import (
    EstadoInscripcion, TipoActividad, TipoRecurso,
    ProgramaNivel, GrupoSeccion, CursoMateria,
    InscripcionCurso, UnidadAcademica, LeccionActividad, RecursoMaterial
)

# --- ESTADO INSCRIPCION ---
class EstadoInscripcionListView(ListView):
    model = EstadoInscripcion

class EstadoInscripcionDetailView(DetailView):
    model = EstadoInscripcion

class EstadoInscripcionCreateView(CreateView):
    model = EstadoInscripcion
    fields = ['nombre_estado']
    template_name = 'academia/nuevo_estado_inscripcion.html'
    success_url = '/academia/estados-inscripcion/'

class EstadoInscripcionUpdateView(UpdateView):
    model = EstadoInscripcion
    fields = ['nombre_estado']
    template_name = 'academia/editar_estado_inscripcion.html'
    success_url = '/academia/estados-inscripcion/'

class EstadoInscripcionDeleteView(DeleteView):
    model = EstadoInscripcion
    success_url = '/academia/estados-inscripcion/'


# --- TIPO ACTIVIDAD ---
class TipoActividadListView(ListView):
    model = TipoActividad

class TipoActividadDetailView(DetailView):
    model = TipoActividad

class TipoActividadCreateView(CreateView):
    model = TipoActividad
    fields = ['nombre_tipo']
    template_name = 'academia/nuevo_tipo_actividad.html'
    success_url = '/academia/tipos-actividad/'

class TipoActividadUpdateView(UpdateView):
    model = TipoActividad
    fields = ['nombre_tipo']
    template_name = 'academia/editar_tipo_actividad.html'
    success_url = '/academia/tipos-actividad/'

class TipoActividadDeleteView(DeleteView):
    model = TipoActividad
    success_url = '/academia/tipos-actividad/'


# --- TIPO RECURSO ---
class TipoRecursoListView(ListView):
    model = TipoRecurso

class TipoRecursoDetailView(DetailView):
    model = TipoRecurso

class TipoRecursoCreateView(CreateView):
    model = TipoRecurso
    fields = ['nombre_tipo']
    template_name = 'academia/nuevo_tipo_recurso.html'
    success_url = '/academia/tipos-recurso/'

class TipoRecursoUpdateView(UpdateView):
    model = TipoRecurso
    fields = ['nombre_tipo']
    template_name = 'academia/editar_tipo_recurso.html'
    success_url = '/academia/tipos-recurso/'

class TipoRecursoDeleteView(DeleteView):
    model = TipoRecurso
    success_url = '/academia/tipos-recurso/'


# --- PROGRAMA NIVEL ---
class ProgramaNivelListView(ListView):
    model = ProgramaNivel

class ProgramaNivelDetailView(DetailView):
    model = ProgramaNivel

class ProgramaNivelCreateView(CreateView):
    model = ProgramaNivel
    fields = ['id_institucion', 'nombre_nivel', 'clave_programa', 'duracion_periodos']
    template_name = 'academia/nuevo_programa.html'
    success_url = '/academia/programas/'

class ProgramaNivelUpdateView(UpdateView):
    model = ProgramaNivel
    fields = ['id_institucion', 'nombre_nivel', 'clave_programa', 'duracion_periodos']
    template_name = 'academia/editar_programa.html'
    success_url = '/academia/programas/'

class ProgramaNivelDeleteView(DeleteView):
    model = ProgramaNivel
    success_url = '/academia/programas/'


# --- GRUPO SECCION ---
class GrupoSeccionListView(ListView):
    model = GrupoSeccion

class GrupoSeccionDetailView(DetailView):
    model = GrupoSeccion

class GrupoSeccionCreateView(CreateView):
    model = GrupoSeccion
    fields = ['id_sede', 'id_docente_titular', 'nombre_grupo', 'grado_semestre', 'ciclo_escolar', 'capacidad_maxima']
    template_name = 'academia/nuevo_grupo.html'
    success_url = '/academia/grupos/'

class GrupoSeccionUpdateView(UpdateView):
    model = GrupoSeccion
    fields = ['id_sede', 'id_docente_titular', 'nombre_grupo', 'grado_semestre', 'ciclo_escolar', 'capacidad_maxima']
    template_name = 'academia/editar_grupo.html'
    success_url = '/academia/grupos/'

class GrupoSeccionDeleteView(DeleteView):
    model = GrupoSeccion
    success_url = '/academia/grupos/'


# --- CURSO MATERIA ---
class CursoMateriaListView(ListView):
    model = CursoMateria

class CursoMateriaDetailView(DetailView):
    model = CursoMateria

class CursoMateriaCreateView(CreateView):
    model = CursoMateria
    fields = ['id_grupo', 'id_docente', 'nombre_materia', 'clave_materia', 'creditos', 'sala_aula', 'horario_resumen']
    template_name = 'academia/nuevo_curso.html'
    success_url = '/academia/cursos/'

class CursoMateriaUpdateView(UpdateView):
    model = CursoMateria
    fields = ['id_grupo', 'id_docente', 'nombre_materia', 'clave_materia', 'creditos', 'sala_aula', 'horario_resumen']
    template_name = 'academia/editar_curso.html'
    success_url = '/academia/cursos/'

class CursoMateriaDeleteView(DeleteView):
    model = CursoMateria
    success_url = '/academia/cursos/'


# --- INSCRIPCION CURSO ---
class InscripcionCursoListView(ListView):
    model = InscripcionCurso

class InscripcionCursoDetailView(DetailView):
    model = InscripcionCurso

class InscripcionCursoCreateView(CreateView):
    model = InscripcionCurso
    fields = ['id_alumno', 'id_curso', 'id_estado_inscripcion', 'progreso_porcentaje']
    template_name = 'academia/nuevo_inscripcion.html'
    success_url = '/academia/inscripciones/'

class InscripcionCursoUpdateView(UpdateView):
    model = InscripcionCurso
    fields = ['id_estado_inscripcion', 'progreso_porcentaje']
    template_name = 'academia/editar_inscripcion.html'
    success_url = '/academia/inscripciones/'

class InscripcionCursoDeleteView(DeleteView):
    model = InscripcionCurso
    success_url = '/academia/inscripciones/'


# --- UNIDAD ACADEMICA ---
class UnidadAcademicaListView(ListView):
    model = UnidadAcademica

class UnidadAcademicaDetailView(DetailView):
    model = UnidadAcademica

class UnidadAcademicaCreateView(CreateView):
    model = UnidadAcademica
    fields = ['id_curso', 'numero_unidad', 'titulo_unidad', 'descripcion']
    template_name = 'academia/nuevo_unidad.html'
    success_url = '/academia/unidades/'

class UnidadAcademicaUpdateView(UpdateView):
    model = UnidadAcademica
    fields = ['id_curso', 'numero_unidad', 'titulo_unidad', 'descripcion']
    template_name = 'academia/editar_unidad.html'
    success_url = '/academia/unidades/'

class UnidadAcademicaDeleteView(DeleteView):
    model = UnidadAcademica
    success_url = '/academia/unidades/'


# --- LECCION ACTIVIDAD ---
class LeccionActividadListView(ListView):
    model = LeccionActividad

class LeccionActividadDetailView(DetailView):
    model = LeccionActividad

class LeccionActividadCreateView(CreateView):
    model = LeccionActividad
    fields = ['id_unidad', 'id_tipo_actividad', 'titulo', 'descripcion_instrucciones', 'puntaje_maximo', 'fecha_apertura', 'fecha_limite', 'estado_publicacion']
    template_name = 'academia/nuevo_leccion.html'
    success_url = '/academia/lecciones/'

class LeccionActividadUpdateView(UpdateView):
    model = LeccionActividad
    fields = ['id_unidad', 'id_tipo_actividad', 'titulo', 'descripcion_instrucciones', 'puntaje_maximo', 'fecha_apertura', 'fecha_limite', 'estado_publicacion']
    template_name = 'academia/editar_leccion.html'
    success_url = '/academia/lecciones/'

class LeccionActividadDeleteView(DeleteView):
    model = LeccionActividad
    success_url = '/academia/lecciones/'


# --- RECURSO MATERIAL ---
class RecursoMaterialListView(ListView):
    model = RecursoMaterial

class RecursoMaterialDetailView(DetailView):
    model = RecursoMaterial

class RecursoMaterialCreateView(CreateView):
    model = RecursoMaterial
    fields = ['id_leccion', 'id_tipo_recurso', 'nombre_recurso', 'url_archivo']
    template_name = 'academia/nuevo_recurso.html'
    success_url = '/academia/recursos/'

class RecursoMaterialUpdateView(UpdateView):
    model = RecursoMaterial
    fields = ['id_leccion', 'id_tipo_recurso', 'nombre_recurso', 'url_archivo']
    template_name = 'academia/editar_recurso.html'
    success_url = '/academia/recursos/'

class RecursoMaterialDeleteView(DeleteView):
    model = RecursoMaterial
    success_url = '/academia/recursos/'