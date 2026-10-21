from django.urls import path
from .views import (
    # Catálogos
    EstadoInscripcionListView, EstadoInscripcionDetailView, EstadoInscripcionCreateView, EstadoInscripcionUpdateView, EstadoInscripcionDeleteView,
    TipoActividadListView, TipoActividadDetailView, TipoActividadCreateView, TipoActividadUpdateView, TipoActividadDeleteView,
    TipoRecursoListView, TipoRecursoDetailView, TipoRecursoCreateView, TipoRecursoUpdateView, TipoRecursoDeleteView,
    # Entidades Principales
    ProgramaNivelListView, ProgramaNivelDetailView, ProgramaNivelCreateView, ProgramaNivelUpdateView, ProgramaNivelDeleteView,
    GrupoSeccionListView, GrupoSeccionDetailView, GrupoSeccionCreateView, GrupoSeccionUpdateView, GrupoSeccionDeleteView,
    CursoMateriaListView, CursoMateriaDetailView, CursoMateriaCreateView, CursoMateriaUpdateView, CursoMateriaDeleteView,
    InscripcionCursoListView, InscripcionCursoDetailView, InscripcionCursoCreateView, InscripcionCursoUpdateView, InscripcionCursoDeleteView,
    UnidadAcademicaListView, UnidadAcademicaDetailView, UnidadAcademicaCreateView, UnidadAcademicaUpdateView, UnidadAcademicaDeleteView,
    LeccionActividadListView, LeccionActividadDetailView, LeccionActividadCreateView, LeccionActividadUpdateView, LeccionActividadDeleteView,
    RecursoMaterialListView, RecursoMaterialDetailView, RecursoMaterialCreateView, RecursoMaterialUpdateView, RecursoMaterialDeleteView,
)

urlpatterns = [
    # Ruta principal (/academia/) -> Redirige a la lista de programas
    path('', ProgramaNivelListView.as_view(), name='academia_index'),

    # --- PROGRAMA NIVEL ---
    path('programas/', ProgramaNivelListView.as_view(), name='programanivel_list'),
    path('programas/<uuid:pk>/', ProgramaNivelDetailView.as_view(), name='programanivel_detail'),
    path('programas/nuevo/', ProgramaNivelCreateView.as_view(), name='programanivel_create'),
    path('programas/<uuid:pk>/editar/', ProgramaNivelUpdateView.as_view(), name='programanivel_update'),
    path('programas/<uuid:pk>/eliminar/', ProgramaNivelDeleteView.as_view(), name='programanivel_delete'),

    # --- GRUPO SECCIÓN ---
    path('grupos/', GrupoSeccionListView.as_view(), name='gruposeccion_list'),
    path('grupos/<uuid:pk>/', GrupoSeccionDetailView.as_view(), name='gruposeccion_detail'),
    path('grupos/nuevo/', GrupoSeccionCreateView.as_view(), name='gruposeccion_create'),
    path('grupos/<uuid:pk>/editar/', GrupoSeccionUpdateView.as_view(), name='gruposeccion_update'),
    path('grupos/<uuid:pk>/eliminar/', GrupoSeccionDeleteView.as_view(), name='gruposeccion_delete'),

    # --- CURSO MATERIA ---
    path('cursos/', CursoMateriaListView.as_view(), name='cursomateria_list'),
    path('cursos/<uuid:pk>/', CursoMateriaDetailView.as_view(), name='cursomateria_detail'),
    path('cursos/nuevo/', CursoMateriaCreateView.as_view(), name='cursomateria_create'),
    path('cursos/<uuid:pk>/editar/', CursoMateriaUpdateView.as_view(), name='cursomateria_update'),
    path('cursos/<uuid:pk>/eliminar/', CursoMateriaDeleteView.as_view(), name='cursomateria_delete'),

    # --- INSCRIPCIÓN CURSO ---
    path('inscripciones/', InscripcionCursoListView.as_view(), name='inscripcioncurso_list'),
    path('inscripciones/<uuid:pk>/', InscripcionCursoDetailView.as_view(), name='inscripcioncurso_detail'),
    path('inscripciones/nueva/', InscripcionCursoCreateView.as_view(), name='inscripcioncurso_create'),
    path('inscripciones/<uuid:pk>/editar/', InscripcionCursoUpdateView.as_view(), name='inscripcioncurso_update'),
    path('inscripciones/<uuid:pk>/eliminar/', InscripcionCursoDeleteView.as_view(), name='inscripcioncurso_delete'),

    # --- UNIDAD ACADÉMICA ---
    path('unidades/', UnidadAcademicaListView.as_view(), name='unidadacademica_list'),
    path('unidades/<uuid:pk>/', UnidadAcademicaDetailView.as_view(), name='unidadacademica_detail'),
    path('unidades/nueva/', UnidadAcademicaCreateView.as_view(), name='unidadacademica_create'),
    path('unidades/<uuid:pk>/editar/', UnidadAcademicaUpdateView.as_view(), name='unidadacademica_update'),
    path('unidades/<uuid:pk>/eliminar/', UnidadAcademicaDeleteView.as_view(), name='unidadacademica_delete'),

    # --- LECCIÓN ACTIVIDAD ---
    path('lecciones/', LeccionActividadListView.as_view(), name='leccionactividad_list'),
    path('lecciones/<uuid:pk>/', LeccionActividadDetailView.as_view(), name='leccionactividad_detail'),
    path('lecciones/nueva/', LeccionActividadCreateView.as_view(), name='leccionactividad_create'),
    path('lecciones/<uuid:pk>/editar/', LeccionActividadUpdateView.as_view(), name='leccionactividad_update'),
    path('lecciones/<uuid:pk>/eliminar/', LeccionActividadDeleteView.as_view(), name='leccionactividad_delete'),

    # --- RECURSO MATERIAL ---
    path('recursos/', RecursoMaterialListView.as_view(), name='recursomaterial_list'),
    path('recursos/<uuid:pk>/', RecursoMaterialDetailView.as_view(), name='recursomaterial_detail'),
    path('recursos/nuevo/', RecursoMaterialCreateView.as_view(), name='recursomaterial_create'),
    path('recursos/<uuid:pk>/editar/', RecursoMaterialUpdateView.as_view(), name='recursomaterial_update'),
    path('recursos/<uuid:pk>/eliminar/', RecursoMaterialDeleteView.as_view(), name='recursomaterial_delete'),

    # --- CATÁLOGOS ---
    path('estados-inscripcion/', EstadoInscripcionListView.as_view(), name='estadoinscripcion_list'),
    path('tipos-actividad/', TipoActividadListView.as_view(), name='tipoactividad_list'),
    path('tipos-recurso/', TipoRecursoListView.as_view(), name='tiporecurso_list'),
]