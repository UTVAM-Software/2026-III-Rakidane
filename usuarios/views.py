from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import (
    RolCuenta, EstadoMatricula, ParentescoTutor, CuentaAcceso,
    Docente, Alumno, TutorPadre, SupervisionTutor
)

# --- ROL CUENTA ---
class RolCuentaListView(ListView):
    model = RolCuenta
    template_name = 'usuarios/Roles/rolcuenta_list.html'
    context_object_name = 'roles'

class RolCuentaDetailView(DetailView):
    model = RolCuenta
    template_name = 'usuarios/Roles/rolcuenta_detail.html'
    context_object_name = 'rol'

class RolCuentaCreateView(CreateView):
    model = RolCuenta
    fields = ['nombre_rol', 'descripcion']
    template_name = 'usuarios/Roles/nuevo_rolcuenta.html'
    success_url = '/usuarios/roles/'

class RolCuentaUpdateView(UpdateView):
    model = RolCuenta
    fields = ['nombre_rol', 'descripcion']
    template_name = 'usuarios/Roles/editar_rolcuenta.html'
    success_url = '/usuarios/roles/'

class RolCuentaDeleteView(DeleteView):
    model = RolCuenta
    template_name = 'usuarios/Roles/rolcuenta_confirm_delete.html'
    success_url = '/usuarios/roles/'


# --- ESTADO MATRICULA ---
class EstadoMatriculaListView(ListView):
    model = EstadoMatricula
    template_name = 'usuarios/Estado_matricula/estadomatricula_list.html'

class EstadoMatriculaDetailView(DetailView):
    model = EstadoMatricula
    template_name = 'usuarios/Estado_matricula/estadomatricula_detail.html'

class EstadoMatriculaCreateView(CreateView):
    model = EstadoMatricula
    fields = ['nombre_estado', 'descripcion']
    template_name = 'usuarios/Estado_matricula/nuevo_estadomatricula.html'
    success_url = '/usuarios/estados-matricula/'

class EstadoMatriculaUpdateView(UpdateView):
    model = EstadoMatricula
    fields = ['nombre_estado', 'descripcion']
    template_name = 'usuarios/Estado_matricula/editar_estadomatricula.html'
    success_url = '/usuarios/estados-matricula/'

class EstadoMatriculaDeleteView(DeleteView):
    model = EstadoMatricula
    template_name = 'usuarios/Estado_matricula/estadomatricula_confirm_delete.html'
    success_url = '/usuarios/estados-matricula/'


# --- PARENTESCO TUTOR ---
class ParentescoTutorListView(ListView):
    model = ParentescoTutor
    template_name = 'usuarios/Parentesco/parentesco_list.html'

class ParentescoTutorDetailView(DetailView):
    model = ParentescoTutor
    template_name = 'usuarios/Parentesco/parentesco_detail.html'

class ParentescoTutorCreateView(CreateView):
    model = ParentescoTutor
    fields = ['nombre_parentesco']
    template_name = 'usuarios/Parentesco/nuevo_parentesco.html'
    success_url = '/usuarios/parentescos/'

class ParentescoTutorUpdateView(UpdateView):
    model = ParentescoTutor
    fields = ['nombre_parentesco']
    template_name = 'usuarios/Parentesco/editar_parentesco.html'
    success_url = '/usuarios/parentescos/'

class ParentescoTutorDeleteView(DeleteView):
    model = ParentescoTutor
    template_name = 'usuarios/Parentesco/parentesco_confirm_delete.html'
    success_url = '/usuarios/parentescos/'


# --- CUENTA ACCESO ---
class CuentaAccesoListView(ListView):
    model = CuentaAcceso
    template_name = 'usuarios/Cuenta_acceso/cuentaacceso_list.html'
    context_object_name = 'cuentas'

class CuentaAccesoDetailView(DetailView):
    model = CuentaAcceso
    template_name = 'usuarios/Cuenta_acceso/cuentaacceso_detail.html'
    context_object_name = 'cuenta'

class CuentaAccesoCreateView(CreateView):
    model = CuentaAcceso
    fields = ['email', 'id_rol', 'proveedor_sso', 'esta_activo']
    template_name = 'usuarios/Cuenta_acceso/nuevo_cuentaacceso.html'
    success_url = '/usuarios/cuentas/'

class CuentaAccesoUpdateView(UpdateView):
    model = CuentaAcceso
    fields = ['email', 'id_rol', 'proveedor_sso', 'esta_activo']
    template_name = 'usuarios/Cuenta_acceso/editar_cuentaacceso.html'
    success_url = '/usuarios/cuentas/'

class CuentaAccesoDeleteView(DeleteView):
    model = CuentaAcceso
    template_name = 'usuarios/Cuenta_acceso/cuentaacceso_confirm_delete.html'
    success_url = '/usuarios/cuentas/'


# --- DOCENTE ---
class DocenteListView(ListView):
    model = Docente
    template_name = 'usuarios/Docentes/docente_list.html'
    context_object_name = 'docentes'

class DocenteDetailView(DetailView):
    model = Docente
    template_name = 'usuarios/Docentes/docente_detail.html'
    context_object_name = 'docente'

class DocenteCreateView(CreateView):
    model = Docente
    fields = [
        'id_cuenta', 'nombres', 'apellido_paterno', 'apellido_materno',
        'numero_empleado', 'cedula_profesional', 'curp_dni', 'fecha_nacimiento',
        'genero', 'telefono_movil', 'departamento', 'especialidad_academica', 'foto_perfil_url'
    ]
    template_name = 'usuarios/Docentes/nuevo_docente.html'
    success_url = '/usuarios/docentes/'

class DocenteUpdateView(UpdateView):
    model = Docente
    fields = [
        'nombres', 'apellido_paterno', 'apellido_materno', 'numero_empleado',
        'cedula_profesional', 'curp_dni', 'fecha_nacimiento', 'genero',
        'telefono_movil', 'departamento', 'especialidad_academica', 'foto_perfil_url'
    ]
    template_name = 'usuarios/Docentes/editar_docente.html'
    success_url = '/usuarios/docentes/'

class DocenteDeleteView(DeleteView):
    model = Docente
    template_name = 'usuarios/Docentes/docente_confirm_delete.html'
    success_url = '/usuarios/docentes/'


# --- ALUMNO ---
class AlumnoListView(ListView):
    model = Alumno
    template_name = 'usuarios/Alumnos/alumno_list.html'
    context_object_name = 'alumnos'

class AlumnoDetailView(DetailView):
    model = Alumno
    template_name = 'usuarios/Alumnos/alumno_detail.html'
    context_object_name = 'alumno'

class AlumnoCreateView(CreateView):
    model = Alumno
    fields = [
        'id_cuenta', 'id_sede', 'id_estado_matricula', 'nombres', 'apellido_paterno',
        'apellido_materno', 'matricula_expediente', 'curp_dni', 'fecha_nacimiento',
        'genero', 'telefono_personal', 'direccion_domicilio', 'foto_perfil_url'
    ]
    template_name = 'usuarios/Alumnos/nuevo_alumno.html'
    success_url = '/usuarios/alumnos/'

class AlumnoUpdateView(UpdateView):
    model = Alumno
    fields = [
        'id_sede', 'id_estado_matricula', 'nombres', 'apellido_paterno',
        'apellido_materno', 'matricula_expediente', 'curp_dni', 'fecha_nacimiento',
        'genero', 'telefono_personal', 'direccion_domicilio', 'foto_perfil_url'
    ]
    template_name = 'usuarios/Alumnos/editar_alumno.html'
    success_url = '/usuarios/alumnos/'

class AlumnoDeleteView(DeleteView):
    model = Alumno
    template_name = 'usuarios/Alumnos/alumno_confirm_delete.html'
    success_url = '/usuarios/alumnos/'


# --- TUTOR PADRE ---
class TutorPadreListView(ListView):
    model = TutorPadre
    template_name = 'usuarios/Tutores_Padres/tutorpadre_list.html'
    context_object_name = 'tutores'

class TutorPadreDetailView(DetailView):
    model = TutorPadre
    template_name = 'usuarios/Tutores_Padres/tutorpadre_detail.html'
    context_object_name = 'tutor'

class TutorPadreCreateView(CreateView):
    model = TutorPadre
    fields = [
        'id_cuenta', 'id_parentesco', 'nombres', 'apellido_paterno',
        'apellido_materno', 'telefono_contacto', 'telefono_emergencia', 'ocupacion'
    ]
    template_name = 'usuarios/Tutores_Padres/nuevo_tutor.html'
    success_url = '/usuarios/tutores/'

class TutorPadreUpdateView(UpdateView):
    model = TutorPadre
    fields = [
        'id_parentesco', 'nombres', 'apellido_paterno', 'apellido_materno',
        'telefono_contacto', 'telefono_emergencia', 'ocupacion'
    ]
    template_name = 'usuarios/Tutores_Padres/editar_tutor.html'
    success_url = '/usuarios/tutores/'

class TutorPadreDeleteView(DeleteView):
    model = TutorPadre
    template_name = 'usuarios/Tutores_Padres/tutorpadre_confirm_delete.html'
    success_url = '/usuarios/tutores/'


# --- SUPERVISION TUTOR ---
class SupervisionTutorListView(ListView):
    model = SupervisionTutor
    template_name = 'usuarios/supervisiontutor_list.html'

class SupervisionTutorDetailView(DetailView):
    model = SupervisionTutor
    template_name = 'usuarios/supervisiontutor_detail.html'

class SupervisionTutorCreateView(CreateView):
    model = SupervisionTutor
    fields = ['id_tutor', 'id_alumno', 'es_contacto_principal']
    template_name = 'usuarios/nuevo_supervisiontutor.html'
    success_url = '/usuarios/supervisiones/'

class SupervisionTutorUpdateView(UpdateView):
    model = SupervisionTutor
    fields = ['id_tutor', 'id_alumno', 'es_contacto_principal']
    template_name = 'usuarios/editar_supervisiontutor.html'
    success_url = '/usuarios/supervisiones/'

class SupervisionTutorDeleteView(DeleteView):
    model = SupervisionTutor
    template_name = 'usuarios/supervisiontutor_confirm_delete.html'
    success_url = '/usuarios/supervisiones/'