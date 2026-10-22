from django.contrib import admin
from .models import (
    CuentaAcceso,
    Alumno,
    Docente,
    TutorPadre,
    EstadoMatricula,
    RolCuenta,
    ParentescoTutor,
    SupervisionTutor,
)

# --- REGISTRO DE CATÁLOGOS ---
@admin.register(RolCuenta)
class RolCuentaAdmin(admin.ModelAdmin):
    list_display = ('nombre_rol', 'descripcion')

@admin.register(EstadoMatricula)
class EstadoMatriculaAdmin(admin.ModelAdmin):
    list_display = ('nombre_estado', 'descripcion')

@admin.register(ParentescoTutor)
class ParentescoTutorAdmin(admin.ModelAdmin):
    list_display = ('nombre_parentesco',)

# --- TABLAS PRINCIPALES ---
@admin.register(CuentaAcceso)
class CuentaAccesoAdmin(admin.ModelAdmin):
    list_display = ('email', 'id_rol', 'esta_activo', 'ultimo_ingreso', 'creado_en')
    list_filter = ('id_rol', 'esta_activo', 'proveedor_sso')
    search_fields = ('email',)

@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellido_paterno', 'numero_empleado', 'departamento')
    search_fields = ('nombres', 'apellido_paterno', 'numero_empleado', 'curp_dni')

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('matricula_expediente', 'nombres', 'apellido_paterno', 'id_estado_matricula', 'id_sede')
    list_filter = ('id_estado_matricula', 'id_sede')
    search_fields = ('matricula_expediente', 'nombres', 'apellido_paterno', 'curp_dni')

@admin.register(TutorPadre)
class TutorPadreAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellido_paterno', 'id_parentesco', 'telefono_contacto')
    search_fields = ('nombres', 'apellido_paterno', 'telefono_contacto')

@admin.register(SupervisionTutor)
class SupervisionTutorAdmin(admin.ModelAdmin):
    list_display = ('id_tutor', 'id_alumno', 'es_contacto_principal')