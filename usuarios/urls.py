from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import permission_required, login_required
from .views import (
    RegistroPublicoView,
    CustomLogoutView,
    RolCuentaListView, RolCuentaDetailView, RolCuentaCreateView, RolCuentaUpdateView, RolCuentaDeleteView,
    EstadoMatriculaListView, EstadoMatriculaDetailView, EstadoMatriculaCreateView, EstadoMatriculaUpdateView, EstadoMatriculaDeleteView,
    ParentescoTutorListView, ParentescoTutorDetailView, ParentescoTutorCreateView, ParentescoTutorUpdateView, ParentescoTutorDeleteView,
    CuentaAccesoListView, CuentaAccesoDetailView, CuentaAccesoCreateView, CuentaAccesoUpdateView, CuentaAccesoDeleteView,
    DocenteListView, DocenteDetailView, DocenteCreateView, DocenteUpdateView, DocenteDeleteView,
    AlumnoListView, AlumnoDetailView, AlumnoCreateView, AlumnoUpdateView, AlumnoDeleteView,
    TutorPadreListView, TutorPadreDetailView, TutorPadreCreateView, TutorPadreUpdateView, TutorPadreDeleteView,
    SupervisionTutorListView, SupervisionTutorDetailView, SupervisionTutorCreateView, SupervisionTutorUpdateView, SupervisionTutorDeleteView,
)

urlpatterns = [
    # --- REGISTRO PÚBLICO ---
    path('registro/', RegistroPublicoView.as_view(), name='registro_publico'),

    # --- AUTENTICACIÓN (LOGIN / LOGOUT) ---
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),

    # --- ALUMNO ---
    path('alumnos/', login_required(AlumnoListView.as_view()), name='alumno_list'),
    path('alumnos/create/', permission_required('usuarios.add_alumno')(AlumnoCreateView.as_view()), name='alumno_create'),
    path('alumnos/<uuid:pk>/', login_required(AlumnoDetailView.as_view()), name='alumno_detail'),
    path('alumnos/<uuid:pk>/update/', permission_required('usuarios.change_alumno')(AlumnoUpdateView.as_view()), name='alumno_update'),
    path('alumnos/<uuid:pk>/delete/', permission_required('usuarios.delete_alumno')(AlumnoDeleteView.as_view()), name='alumno_delete'),

    # --- DOCENTE ---
    path('docentes/', login_required(DocenteListView.as_view()), name='docente_list'),
    path('docentes/create/', permission_required('usuarios.add_docente')(DocenteCreateView.as_view()), name='docente_create'),
    path('docentes/<uuid:pk>/', login_required(DocenteDetailView.as_view()), name='docente_detail'),
    path('docentes/<uuid:pk>/update/', permission_required('usuarios.change_docente')(DocenteUpdateView.as_view()), name='docente_update'),
    path('docentes/<uuid:pk>/delete/', permission_required('usuarios.delete_docente')(DocenteDeleteView.as_view()), name='docente_delete'),

    # --- TUTOR PADRE ---
    path('tutores/', login_required(TutorPadreListView.as_view()), name='tutorpadre_list'),
    path('tutores/create/', permission_required('usuarios.add_tutorpadre')(TutorPadreCreateView.as_view()), name='tutorpadre_create'),
    path('tutores/<uuid:pk>/', login_required(TutorPadreDetailView.as_view()), name='tutorpadre_detail'),
    path('tutores/<uuid:pk>/update/', permission_required('usuarios.change_tutorpadre')(TutorPadreUpdateView.as_view()), name='tutorpadre_update'),
    path('tutores/<uuid:pk>/delete/', permission_required('usuarios.delete_tutorpadre')(TutorPadreDeleteView.as_view()), name='tutorpadre_delete'),

    # --- CUENTA ACCESO ---
    path('cuentas/', login_required(CuentaAccesoListView.as_view()), name='cuentaacceso_list'),
    path('cuentas/create/', permission_required('usuarios.add_cuentaacceso')(CuentaAccesoCreateView.as_view()), name='cuentaacceso_create'),
    path('cuentas/<uuid:pk>/', login_required(CuentaAccesoDetailView.as_view()), name='cuentaacceso_detail'),
    path('cuentas/<uuid:pk>/update/', permission_required('usuarios.change_cuentaacceso')(CuentaAccesoUpdateView.as_view()), name='cuentaacceso_update'),
    path('cuentas/<uuid:pk>/delete/', permission_required('usuarios.delete_cuentaacceso')(CuentaAccesoDeleteView.as_view()), name='cuentaacceso_delete'),

    # --- ROL CUENTA ---
    path('roles/', login_required(RolCuentaListView.as_view()), name='rol_list'),
    path('roles/create/', permission_required('usuarios.add_rolcuenta')(RolCuentaCreateView.as_view()), name='rol_create'),
    path('roles/<uuid:pk>/', login_required(RolCuentaDetailView.as_view()), name='rol_detail'),
    path('roles/<uuid:pk>/update/', permission_required('usuarios.change_rolcuenta')(RolCuentaUpdateView.as_view()), name='rol_update'),
    path('roles/<uuid:pk>/delete/', permission_required('usuarios.delete_rolcuenta')(RolCuentaDeleteView.as_view()), name='rol_delete'),

    # --- ESTADO MATRICULA ---
    path('estados-matricula/', login_required(EstadoMatriculaListView.as_view()), name='estadomatricula_list'),
    path('estados-matricula/create/', permission_required('usuarios.add_estadomatricula')(EstadoMatriculaCreateView.as_view()), name='estadomatricula_create'),
    path('estados-matricula/<uuid:pk>/', login_required(EstadoMatriculaDetailView.as_view()), name='estadomatricula_detail'),
    path('estados-matricula/<uuid:pk>/update/', permission_required('usuarios.change_estadomatricula')(EstadoMatriculaUpdateView.as_view()), name='estadomatricula_update'),
    path('estados-matricula/<uuid:pk>/delete/', permission_required('usuarios.delete_estadomatricula')(EstadoMatriculaDeleteView.as_view()), name='estadomatricula_delete'),

    # --- PARENTESCO TUTOR ---
    path('parentescos/', login_required(ParentescoTutorListView.as_view()), name='parentescomodel_list'),
    path('parentescos/create/', permission_required('usuarios.add_parentescotutor')(ParentescoTutorCreateView.as_view()), name='parentescomodel_create'),
    path('parentescos/<uuid:pk>/', login_required(ParentescoTutorDetailView.as_view()), name='parentescomodel_detail'),
    path('parentescos/<uuid:pk>/update/', permission_required('usuarios.change_parentescotutor')(ParentescoTutorUpdateView.as_view()), name='parentescomodel_update'),
    path('parentescos/<uuid:pk>/delete/', permission_required('usuarios.delete_parentescotutor')(ParentescoTutorDeleteView.as_view()), name='parentescomodel_delete'),

    # --- SUPERVISION TUTOR ---
    path('supervisiones/', login_required(SupervisionTutorListView.as_view()), name='supervisiontutor_list'),
    path('supervisiones/create/', permission_required('usuarios.add_supervisiontutor')(SupervisionTutorCreateView.as_view()), name='supervisiontutor_create'),
    path('supervisiones/<int:pk>/', login_required(SupervisionTutorDetailView.as_view()), name='supervisiontutor_detail'),
    path('supervisiones/<int:pk>/update/', permission_required('usuarios.change_supervisiontutor')(SupervisionTutorUpdateView.as_view()), name='supervisiontutor_update'),
    path('supervisiones/<int:pk>/delete/', permission_required('usuarios.delete_supervisiontutor')(SupervisionTutorDeleteView.as_view()), name='supervisiontutor_delete'),
]