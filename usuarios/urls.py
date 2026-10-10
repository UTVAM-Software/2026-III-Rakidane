from django.urls import path
from .views import (
    # RolCuenta
    RolCuentaListView, RolCuentaDetailView, RolCuentaCreateView, RolCuentaUpdateView, RolCuentaDeleteView,
    # EstadoMatricula
    EstadoMatriculaListView, EstadoMatriculaDetailView, EstadoMatriculaCreateView, EstadoMatriculaUpdateView, EstadoMatriculaDeleteView,
    # ParentescoTutor
    ParentescoTutorListView, ParentescoTutorDetailView, ParentescoTutorCreateView, ParentescoTutorUpdateView, ParentescoTutorDeleteView,
    # CuentaAcceso
    CuentaAccesoListView, CuentaAccesoDetailView, CuentaAccesoCreateView, CuentaAccesoUpdateView, CuentaAccesoDeleteView,
    # Docente
    DocenteListView, DocenteDetailView, DocenteCreateView, DocenteUpdateView, DocenteDeleteView,
    # Alumno
    AlumnoListView, AlumnoDetailView, AlumnoCreateView, AlumnoUpdateView, AlumnoDeleteView,
    # TutorPadre
    TutorPadreListView, TutorPadreDetailView, TutorPadreCreateView, TutorPadreUpdateView, TutorPadreDeleteView,
    # SupervisionTutor
    SupervisionTutorListView, SupervisionTutorDetailView, SupervisionTutorCreateView, SupervisionTutorUpdateView, SupervisionTutorDeleteView,
)

urlpatterns = [
    # Alumno
    path('alumnos/', AlumnoListView.as_view(), name='alumno_list'),
    path('alumnos/create/', AlumnoCreateView.as_view(), name='alumno_create'),
    path('alumnos/<uuid:pk>/', AlumnoDetailView.as_view(), name='alumno_detail'),
    path('alumnos/<uuid:pk>/update/', AlumnoUpdateView.as_view(), name='alumno_update'),
    path('alumnos/<uuid:pk>/delete/', AlumnoDeleteView.as_view(), name='alumno_delete'),

    # Docente
    path('docentes/', DocenteListView.as_view(), name='docente_list'),
    path('docentes/create/', DocenteCreateView.as_view(), name='docente_create'),
    path('docentes/<uuid:pk>/', DocenteDetailView.as_view(), name='docente_detail'),
    path('docentes/<uuid:pk>/update/', DocenteUpdateView.as_view(), name='docente_update'),
    path('docentes/<uuid:pk>/delete/', DocenteDeleteView.as_view(), name='docente_delete'),

    # TutorPadre
    path('tutores/', TutorPadreListView.as_view(), name='tutorpadre_list'),
    path('tutores/create/', TutorPadreCreateView.as_view(), name='tutorpadre_create'),
    path('tutores/<uuid:pk>/', TutorPadreDetailView.as_view(), name='tutorpadre_detail'),
    path('tutores/<uuid:pk>/update/', TutorPadreUpdateView.as_view(), name='tutorpadre_update'),
    path('tutores/<uuid:pk>/delete/', TutorPadreDeleteView.as_view(), name='tutorpadre_delete'),

    # CuentaAcceso
    path('cuentas/', CuentaAccesoListView.as_view(), name='cuentaacceso_list'),
    path('cuentas/create/', CuentaAccesoCreateView.as_view(), name='cuentaacceso_create'),
    path('cuentas/<uuid:pk>/', CuentaAccesoDetailView.as_view(), name='cuentaacceso_detail'),
    path('cuentas/<uuid:pk>/update/', CuentaAccesoUpdateView.as_view(), name='cuentaacceso_update'),
    path('cuentas/<uuid:pk>/delete/', CuentaAccesoDeleteView.as_view(), name='cuentaacceso_delete'),

    # RolCuenta
    path('roles/', RolCuentaListView.as_view(), name='rol_list'),
    path('roles/create/', RolCuentaCreateView.as_view(), name='rol_create'),
    path('roles/<uuid:pk>/', RolCuentaDetailView.as_view(), name='rol_detail'),
    path('roles/<uuid:pk>/update/', RolCuentaUpdateView.as_view(), name='rol_update'),
    path('roles/<uuid:pk>/delete/', RolCuentaDeleteView.as_view(), name='rol_delete'),

    # EstadoMatricula
    path('estados-matricula/', EstadoMatriculaListView.as_view(), name='estadomatricula_list'),
    path('estados-matricula/create/', EstadoMatriculaCreateView.as_view(), name='estadomatricula_create'),
    path('estados-matricula/<uuid:pk>/', EstadoMatriculaDetailView.as_view(), name='estadomatricula_detail'),
    path('estados-matricula/<uuid:pk>/update/', EstadoMatriculaUpdateView.as_view(), name='estadomatricula_update'),
    path('estados-matricula/<uuid:pk>/delete/', EstadoMatriculaDeleteView.as_view(), name='estadomatricula_delete'),

    # ParentescoTutor
    path('parentescos/', ParentescoTutorListView.as_view(), name='parentescomodel_list'),
    path('parentescos/create/', ParentescoTutorCreateView.as_view(), name='parentescomodel_create'),
    path('parentescos/<uuid:pk>/', ParentescoTutorDetailView.as_view(), name='parentescomodel_detail'),
    path('parentescos/<uuid:pk>/update/', ParentescoTutorUpdateView.as_view(), name='parentescomodel_update'),
    path('parentescos/<uuid:pk>/delete/', ParentescoTutorDeleteView.as_view(), name='parentescomodel_delete'),

    # SupervisionTutor
    path('supervisiones/', SupervisionTutorListView.as_view(), name='supervisiontutor_list'),
    path('supervisiones/create/', SupervisionTutorCreateView.as_view(), name='supervisiontutor_create'),
    path('supervisiones/<int:pk>/', SupervisionTutorDetailView.as_view(), name='supervisiontutor_detail'),
    path('supervisiones/<int:pk>/update/', SupervisionTutorUpdateView.as_view(), name='supervisiontutor_update'),
    path('supervisiones/<int:pk>/delete/', SupervisionTutorDeleteView.as_view(), name='supervisiontutor_delete'),
]