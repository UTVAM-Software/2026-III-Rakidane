from django.urls import path
from django.contrib.auth.decorators import permission_required, login_required
from .views import (
    EstadoInscripcionListView, EstadoInscripcionDetailView, EstadoInscripcionCreateView, EstadoInscripcionUpdateView, EstadoInscripcionDeleteView,
    TipoActividadListView, TipoActividadDetailView, TipoActividadCreateView, TipoActividadUpdateView, TipoActividadDeleteView,
    TipoRecursoListView, TipoRecursoDetailView, TipoRecursoCreateView, TipoRecursoUpdateView, TipoRecursoDeleteView,
    ProgramaNivelListView, ProgramaNivelDetailView, ProgramaNivelCreateView, ProgramaNivelUpdateView, ProgramaNivelDeleteView,
    GrupoSeccionListView, GrupoSeccionDetailView, GrupoSeccionCreateView, GrupoSeccionUpdateView, GrupoSeccionDeleteView,
    CursoMateriaListView, CursoMateriaDetailView, CursoMateriaCreateView, CursoMateriaUpdateView, CursoMateriaDeleteView,
    InscripcionCursoListView, InscripcionCursoDetailView, InscripcionCursoCreateView, InscripcionCursoUpdateView, InscripcionCursoDeleteView,
    UnidadAcademicaListView, UnidadAcademicaDetailView, UnidadAcademicaCreateView, UnidadAcademicaUpdateView, UnidadAcademicaDeleteView,
    LeccionActividadListView, LeccionActividadDetailView, LeccionActividadCreateView, LeccionActividadUpdateView, LeccionActividadDeleteView,
    RecursoMaterialListView, RecursoMaterialDetailView, RecursoMaterialCreateView, RecursoMaterialUpdateView, RecursoMaterialDeleteView,
)

urlpatterns = [
    # --- CATÁLOGOS ---
    # EstadoInscripcion
    path('estados-inscripcion/', login_required(EstadoInscripcionListView.as_view()), name='estadoinscripcion_list'),
    path('estados-inscripcion/<uuid:pk>/', login_required(EstadoInscripcionDetailView.as_view()), name='estadoinscripcion_detail'),
    path('estados-inscripcion/create/', permission_required('academia.add_estadoinscripcion')(EstadoInscripcionCreateView.as_view()), name='estadoinscripcion_create'),
    path('estados-inscripcion/<uuid:pk>/update/', permission_required('academia.change_estadoinscripcion')(EstadoInscripcionUpdateView.as_view()), name='estadoinscripcion_update'),
    path('estados-inscripcion/<uuid:pk>/delete/', permission_required('academia.delete_estadoinscripcion')(EstadoInscripcionDeleteView.as_view()), name='estadoinscripcion_delete'),

    # TipoActividad
    path('tipos-actividad/', login_required(TipoActividadListView.as_view()), name='tipoactividad_list'),
    path('tipos-actividad/<uuid:pk>/', login_required(TipoActividadDetailView.as_view()), name='tipoactividad_detail'),
    path('tipos-actividad/create/', permission_required('academia.add_tipoactividad')(TipoActividadCreateView.as_view()), name='tipoactividad_create'),
    path('tipos-actividad/<uuid:pk>/update/', permission_required('academia.change_tipoactividad')(TipoActividadUpdateView.as_view()), name='tipoactividad_update'),
    path('tipos-actividad/<uuid:pk>/delete/', permission_required('academia.delete_tipoactividad')(TipoActividadDeleteView.as_view()), name='tipoactividad_delete'),

    # TipoRecurso
    path('tipos-recurso/', login_required(TipoRecursoListView.as_view()), name='tiporecurso_list'),
    path('tipos-recurso/<uuid:pk>/', login_required(TipoRecursoDetailView.as_view()), name='tiporecurso_detail'),
    path('tipos-recurso/create/', permission_required('academia.add_tiporecurso')(TipoRecursoCreateView.as_view()), name='tiporecurso_create'),
    path('tipos-recurso/<uuid:pk>/update/', permission_required('academia.change_tiporecurso')(TipoRecursoUpdateView.as_view()), name='tiporecurso_update'),
    path('tipos-recurso/<uuid:pk>/delete/', permission_required('academia.delete_tiporecurso')(TipoRecursoDeleteView.as_view()), name='tiporecurso_delete'),

    # --- TABLAS PRINCIPALES ---
    # ProgramaNivel
    path('programas/', login_required(ProgramaNivelListView.as_view()), name='programanivel_list'),
    path('programas/<uuid:pk>/', login_required(ProgramaNivelDetailView.as_view()), name='programanivel_detail'),
    path('programas/create/', permission_required('academia.add_programanivel')(ProgramaNivelCreateView.as_view()), name='programanivel_create'),
    path('programas/<uuid:pk>/update/', permission_required('academia.change_programanivel')(ProgramaNivelUpdateView.as_view()), name='programanivel_update'),
    path('programas/<uuid:pk>/delete/', permission_required('academia.delete_programanivel')(ProgramaNivelDeleteView.as_view()), name='programanivel_delete'),

    # GrupoSeccion
    path('grupos/', login_required(GrupoSeccionListView.as_view()), name='gruposeccion_list'),
    path('grupos/<uuid:pk>/', login_required(GrupoSeccionDetailView.as_view()), name='gruposeccion_detail'),
    path('grupos/create/', permission_required('academia.add_gruposeccion')(GrupoSeccionCreateView.as_view()), name='gruposeccion_create'),
    path('grupos/<uuid:pk>/update/', permission_required('academia.change_gruposeccion')(GrupoSeccionUpdateView.as_view()), name='gruposeccion_update'),
    path('grupos/<uuid:pk>/delete/', permission_required('academia.delete_gruposeccion')(GrupoSeccionDeleteView.as_view()), name='gruposeccion_delete'),

    # CursoMateria
    path('cursos/', login_required(CursoMateriaListView.as_view()), name='cursomateria_list'),
    path('cursos/<uuid:pk>/', login_required(CursoMateriaDetailView.as_view()), name='cursomateria_detail'),
    path('cursos/create/', permission_required('academia.add_cursomateria')(CursoMateriaCreateView.as_view()), name='cursomateria_create'),
    path('cursos/<uuid:pk>/update/', permission_required('academia.change_cursomateria')(CursoMateriaUpdateView.as_view()), name='cursomateria_update'),
    path('cursos/<uuid:pk>/delete/', permission_required('academia.delete_cursomateria')(CursoMateriaDeleteView.as_view()), name='cursomateria_delete'),

    # InscripcionCurso
    path('inscripciones/', login_required(InscripcionCursoListView.as_view()), name='inscripcioncurso_list'),
    path('inscripciones/<uuid:pk>/', login_required(InscripcionCursoDetailView.as_view()), name='inscripcioncurso_detail'),
    path('inscripciones/create/', permission_required('academia.add_inscripcioncurso')(InscripcionCursoCreateView.as_view()), name='inscripcioncurso_create'),
    path('inscripciones/<uuid:pk>/update/', permission_required('academia.change_inscripcioncurso')(InscripcionCursoUpdateView.as_view()), name='inscripcioncurso_update'),
    path('inscripciones/<uuid:pk>/delete/', permission_required('academia.delete_inscripcioncurso')(InscripcionCursoDeleteView.as_view()), name='inscripcioncurso_delete'),

    # UnidadAcademica
    path('unidades/', login_required(UnidadAcademicaListView.as_view()), name='unidadacademica_list'),
    path('unidades/<uuid:pk>/', login_required(UnidadAcademicaDetailView.as_view()), name='unidadacademica_detail'),
    path('unidades/create/', permission_required('academia.add_unidadacademica')(UnidadAcademicaCreateView.as_view()), name='unidadacademica_create'),
    path('unidades/<uuid:pk>/update/', permission_required('academia.change_unidadacademica')(UnidadAcademicaUpdateView.as_view()), name='unidadacademica_update'),
    path('unidades/<uuid:pk>/delete/', permission_required('academia.delete_unidadacademica')(UnidadAcademicaDeleteView.as_view()), name='unidadacademica_delete'),

    # LeccionActividad
    path('lecciones/', login_required(LeccionActividadListView.as_view()), name='leccionactividad_list'),
    path('lecciones/<uuid:pk>/', login_required(LeccionActividadDetailView.as_view()), name='leccionactividad_detail'),
    path('lecciones/create/', permission_required('academia.add_leccionactividad')(LeccionActividadCreateView.as_view()), name='leccionactividad_create'),
    path('lecciones/<uuid:pk>/update/', permission_required('academia.change_leccionactividad')(LeccionActividadUpdateView.as_view()), name='leccionactividad_update'),
    path('lecciones/<uuid:pk>/delete/', permission_required('academia.delete_leccionactividad')(LeccionActividadDeleteView.as_view()), name='leccionactividad_delete'),

    # RecursoMaterial
    path('recursos/', login_required(RecursoMaterialListView.as_view()), name='recursomaterial_list'),
    path('recursos/<uuid:pk>/', login_required(RecursoMaterialDetailView.as_view()), name='recursomaterial_detail'),
    path('recursos/create/', permission_required('academia.add_recursomaterial')(RecursoMaterialCreateView.as_view()), name='recursomaterial_create'),
    path('recursos/<uuid:pk>/update/', permission_required('academia.change_recursomaterial')(RecursoMaterialUpdateView.as_view()), name='recursomaterial_update'),
    path('recursos/<uuid:pk>/delete/', permission_required('academia.delete_recursomaterial')(RecursoMaterialDeleteView.as_view()), name='recursomaterial_delete'),
]
