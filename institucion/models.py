import uuid
from django.db import models

class Institucion(models.Model):
    id_institucion = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre_institucion = models.CharField(max_length=150)
    clave_cct_rvoe = models.CharField(max_length=50, blank=True, null=True, help_text="Clave de Centro de Trabajo o RVOE")
    razon_social = models.CharField(max_length=150, blank=True, null=True)
    rfc_identificador_fiscal = models.CharField(max_length=30, blank=True, null=True)
    direccion_fiscal = models.TextField(blank=True, null=True)
    telefono_contacto = models.CharField(max_length=20, blank=True, null=True)
    email_contacto = models.EmailField(blank=True, null=True)
    logo_url = models.URLField(blank=True, null=True)
    sitio_web = models.URLField(blank=True, null=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'institucion'

    def __str__(self):
        return self.nombre_institucion


class Sede(models.Model):
    id_sede = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE, db_column='id_institucion')
    nombre_sede = models.CharField(max_length=100)
    codigo_campus = models.CharField(max_length=20, blank=True, null=True)
    direccion_calle = models.CharField(max_length=200, blank=True, null=True)
    ciudad = models.CharField(max_length=100, blank=True, null=True)
    estado_provincia = models.CharField(max_length=100, blank=True, null=True)
    codigo_postal = models.CharField(max_length=15, blank=True, null=True)
    pais = models.CharField(max_length=80, default='México')
    telefono_responsable = models.CharField(max_length=20, blank=True, null=True)
    email_responsable = models.EmailField(blank=True, null=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'sede'

    def __str__(self):
        return f"{self.nombre_sede} ({self.id_institucion.nombre_institucion})"


class IntegracionSistema(models.Model):
    id_integracion = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE, db_column='id_institucion')
    tipo_sistema = models.CharField(max_length=50, help_text="Ej: Moodle, Canvas, Google Classroom, Banner")
    credenciales_api_key = models.TextField(blank=True, null=True)
    url_endpoint = models.URLField(blank=True, null=True)
    estado_conexion = models.CharField(max_length=30, default='activo')
    ultima_sincronizacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'integracion_sistema'


class PasoOnboarding(models.Model):
    id_paso = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE, db_column='id_institucion')
    nombre_paso = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    orden_secuencia = models.IntegerField(default=1)
    estado_paso = models.CharField(max_length=30, default='pendiente')
    completado_en = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'paso_onboarding'