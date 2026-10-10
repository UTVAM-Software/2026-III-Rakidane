from django.urls import path
from .views import (
    EstadoInscripcionListView, TipoActividadListView, TipoRecursoListView,
    ProgramaNivelListView, ProgramaNivelDetailView, ProgramaNivelCreateView, ProgramaNivelUpdateView, ProgramaNivelDeleteView,
    GrupoSeccionListView, GrupoSeccionDetailView, GrupoSeccionCreateView, GrupoSeccionUpdateView, GrupoSeccionDeleteView,
    CursoMateriaListView, CursoMateriaDetailView, CursoMateriaCreateView, CursoMateriaUpdateView, CursoMateriaDeleteView,
    InscripcionCursoListView, InscripcionCursoDetailView, InscripcionCursoCreateView, InscripcionCursoUpdateView, InscripcionCursoDeleteView,
    UnidadAcademicaListView, UnidadAcademicaDetailView, UnidadAcademicaCreateView, UnidadAcademicaUpdateView, UnidadAcademicaDeleteView,
    LeccionActividadListView, LeccionActividadDetailView, LeccionActividadCreateView, LeccionActividadUpdateView, LeccionActividadDeleteView,
    RecursoMaterialListView, RecursoMaterialDetailView, RecursoMaterialCreateView, RecursoMaterialUpdateView, RecursoMaterialDeleteView,
)

urlpatterns = [
    # Catálogos
    path('estados-inscripcion/', EstadoInscripcionListView.as_view(), name='estadoinscripcion_list'),
    path('tipos-actividad/', TipoActividadListView.as_view(), name='tipoactividad_list'),
    path('tipos-recurso/', TipoRecursoListView.as_view(), name='tiporecurso_list'),

    # ProgramaNivel
    path('programas/', ProgramaNivelListView.as_view(), name='programanivel_list'),
    path('programas/<uuid:pk>/', ProgramaNivelDetailView.as_view(), name='programanivel_detail'),
    path('programas/create/', ProgramaNivelCreateView.as_view(), name='programanivel_create'),
    path('programas/<uuid:pk>/update/', ProgramaNivelUpdateView.as_view(), name='programanivel_update'),
    path('programas/<uuid:pk>/delete/', ProgramaNivelDeleteView.as_view(), name='programanivel_delete'),

    # GrupoSeccion
    path('grupos/', GrupoSeccionListView.as_view(), name='gruposeccion_list'),
    path('grupos/<uuid:pk>/', GrupoSeccionDetailView.as_view(), name='gruposeccion_detail'),
    path('grupos/create/', GrupoSeccionCreateView.as_view(), name='gruposeccion_create'),
    path('grupos/<uuid:pk>/update/', GrupoSeccionUpdateView.as_view(), name='gruposeccion_update'),
    path('grupos/<uuid:pk>/delete/', GrupoSeccionDeleteView.as_view(), name='gruposeccion_delete'),

    # CursoMateria
    path('cursos/', CursoMateriaListView.as_view(), name='cursomateria_list'),
    path('cursos/<uuid:pk>/', CursoMateriaDetailView.as_view(), name='cursomateria_detail'),
    path('cursos/create/', CursoMateriaCreateView.as_view(), name='cursomateria_create'),
    path('cursos/<uuid:pk>/update/', CursoMateriaUpdateView.as_view(), name='cursomateria_update'),
    path('cursos/<uuid:pk>/delete/', CursoMateriaDeleteView.as_view(), name='cursomateria_delete'),

    # InscripcionCurso
    path('inscripciones/', InscripcionCursoListView.as_view(), name='inscripcioncurso_list'),
    path('inscripciones/<uuid:pk>/', InscripcionCursoDetailView.as_view(), name='inscripcioncurso_detail'),
    path('inscripciones/create/', InscripcionCursoCreateView.as_view(), name='inscripcioncurso_create'),
    path('inscripciones/<uuid:pk>/update/', InscripcionCursoUpdateView.as_view(), name='inscripcioncurso_update'),
    path('inscripciones/<uuid:pk>/delete/', InscripcionCursoDeleteView.as_view(), name='inscripcioncurso_delete'),

    # UnidadAcademica
    path('unidades/', UnidadAcademicaListView.as_view(), name='unidadacademica_list'),
    path('unidades/<uuid:pk>/', UnidadAcademicaDetailView.as_view(), name='unidadacademica_detail'),
    path('unidades/create/', UnidadAcademicaCreateView.as_view(), name='unidadacademica_create'),
    path('unidades/<uuid:pk>/update/', UnidadAcademicaUpdateView.as_view(), name='unidadacademica_update'),
    path('unidades/<uuid:pk>/delete/', UnidadAcademicaDeleteView.as_view(), name='unidadacademica_delete'),

    # LeccionActividad
    path('lecciones/', LeccionActividadListView.as_view(), name='leccionactividad_list'),
    path('lecciones/<uuid:pk>/', LeccionActividadDetailView.as_view(), name='leccionactividad_detail'),
    path('lecciones/create/', LeccionActividadCreateView.as_view(), name='leccionactividad_create'),
    path('lecciones/<uuid:pk>/update/', LeccionActividadUpdateView.as_view(), name='leccionactividad_update'),
    path('lecciones/<uuid:pk>/delete/', LeccionActividadDeleteView.as_view(), name='leccionactividad_delete'),

    # RecursoMaterial
    path('recursos/', RecursoMaterialListView.as_view(), name='recursomaterial_list'),
    path('recursos/<uuid:pk>/', RecursoMaterialDetailView.as_view(), name='recursomaterial_detail'),
    path('recursos/create/', RecursoMaterialCreateView.as_view(), name='recursomaterial_create'),
    path('recursos/<uuid:pk>/update/', RecursoMaterialUpdateView.as_view(), name='recursomaterial_update'),
    path('recursos/<uuid:pk>/delete/', RecursoMaterialDeleteView.as_view(), name='recursomaterial_delete'),
]