import uuid
from django.db import models

# --- CATÁLOGOS REUTILIZABLES ---
class RolCuenta(models.Model):
    id_rol = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre_rol = models.CharField(max_length=50, unique=True, help_text="Superadmin, Admin Institucion, Docente, Alumno, Tutor")
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'rol_cuenta'

    def __str__(self):
        return self.nombre_rol


class EstadoMatricula(models.Model):
    id_estado_matricula = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre_estado = models.CharField(max_length=50, unique=True, help_text="Activo, Baja Temporal, Graduado, Suspendido")
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'estado_matricula'

    def __str__(self):
        return self.nombre_estado


class ParentescoTutor(models.Model):
    id_parentesco = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre_parentesco = models.CharField(max_length=50, unique=True, help_text="Padre, Madre, Tutor Legal, Abuelo/a")

    class Meta:
        db_table = 'parentesco_tutor'

    def __str__(self):
        return self.nombre_parentesco


# --- TABLAS PRINCIPALES ---
class CuentaAcceso(models.Model):
    id_cuenta = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=255, blank=True, null=True)
    id_rol = models.ForeignKey(RolCuenta, on_delete=models.PROTECT, db_column='id_rol', null=True, blank=True)
    proveedor_sso = models.CharField(max_length=50, default='email')
    esta_activo = models.BooleanField(default=True)
    ultimo_ingreso = models.DateTimeField(blank=True, null=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'cuenta_acceso'

    def __str__(self):
        return f"{self.email} [{self.id_rol}]"


class Docente(models.Model):
    id_docente = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_cuenta = models.OneToOneField(CuentaAcceso, on_delete=models.SET_NULL, db_column='id_cuenta', null=True, blank=True)
    nombres = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100, blank=True, null=True)
    numero_empleado = models.CharField(max_length=50, unique=True, blank=True, null=True)
    cedula_profesional = models.CharField(max_length=50, blank=True, null=True)
    curp_dni = models.CharField(max_length=30, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    genero = models.CharField(max_length=20, blank=True, null=True)
    telefono_movil = models.CharField(max_length=20, blank=True, null=True)
    departamento = models.CharField(max_length=100, blank=True, null=True)
    especialidad_academica = models.CharField(max_length=150, blank=True, null=True)
    foto_perfil_url = models.URLField(blank=True, null=True)

    class Meta:
        db_table = 'docente'

    def __str__(self):
        return f"{self.nombres} {self.apellido_paterno} {self.apellido_materno or ''}".strip()


class Alumno(models.Model):
    id_alumno = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_cuenta = models.OneToOneField(CuentaAcceso, on_delete=models.SET_NULL, db_column='id_cuenta', null=True, blank=True)
    id_sede = models.ForeignKey('institucion.Sede', on_delete=models.SET_NULL, null=True, blank=True, db_column='id_sede')
    id_estado_matricula = models.ForeignKey(EstadoMatricula, on_delete=models.PROTECT, db_column='id_estado_matricula', null=True, blank=True)
    nombres = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100, blank=True, null=True)
    matricula_expediente = models.CharField(max_length=50, unique=True)
    curp_dni = models.CharField(max_length=30, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    genero = models.CharField(max_length=20, blank=True, null=True)
    telefono_personal = models.CharField(max_length=20, blank=True, null=True)
    direccion_domicilio = models.TextField(blank=True, null=True)
    foto_perfil_url = models.URLField(blank=True, null=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'alumno'

    def __str__(self):
        return f"{self.matricula_expediente} - {self.nombres} {self.apellido_paterno}"


class TutorPadre(models.Model):
    id_tutor = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_cuenta = models.OneToOneField(CuentaAcceso, on_delete=models.SET_NULL, db_column='id_cuenta', null=True, blank=True)
    id_parentesco = models.ForeignKey(ParentescoTutor, on_delete=models.PROTECT, db_column='id_parentesco', null=True, blank=True)
    nombres = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100, blank=True, null=True)
    telefono_contacto = models.CharField(max_length=20)
    telefono_emergencia = models.CharField(max_length=20, blank=True, null=True)
    ocupacion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'tutor_padre'

    def __str__(self):
        return f"{self.nombres} {self.apellido_paterno}"


class SupervisionTutor(models.Model):
    id_tutor = models.ForeignKey(TutorPadre, on_delete=models.CASCADE, db_column='id_tutor')
    id_alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, db_column='id_alumno')
    es_contacto_principal = models.BooleanField(default=True)

    class Meta:
        db_table = 'supervision_tutor'
        unique_together = (('id_tutor', 'id_alumno'),)