import uuid
from django.db import models

# --- CATÁLOGOS REUTILIZABLES ---
class NivelRiesgo(models.Model):
    id_nivel_riesgo = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre_nivel = models.CharField(max_length=50, unique=True, help_text="Bajo, Medio, Alto, Crítico")
    codigo_color_hex = models.CharField(max_length=7, default="#28A745", help_text="Color para la UI (ej: #FF0000)")
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'nivel_riesgo'

    def __str__(self):
        return self.nombre_nivel


class EstadoValidacionAlerta(models.Model):
    id_estado_valid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre_estado = models.CharField(max_length=50, unique=True, help_text="Pendiente Revision, Confirmado por Docente, Falso Positivo")

    class Meta:
        db_table = 'estado_validacion_alerta'

    def __str__(self):
        return self.nombre_estado


class EstadoAsistencia(models.Model):
    id_estado_asistencia = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre_estado = models.CharField(max_length=50, unique=True, help_text="Presente, Falta, Retardo, Justificado")

    class Meta:
        db_table = 'estado_asistencia'

    def __str__(self):
        return self.nombre_estado


# --- TABLAS PRINCIPALES ---
class PublicacionTablon(models.Model):
    id_publicacion = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_curso = models.ForeignKey('academia.CursoMateria', on_delete=models.CASCADE, db_column='id_curso')
    id_autor = models.ForeignKey('usuarios.CuentaAcceso', on_delete=models.CASCADE, db_column='id_autor', null=True, blank=True)
    titulo = models.CharField(max_length=150, blank=True, null=True)
    contenido_texto = models.TextField()
    fijado_inicio = models.BooleanField(default=False)
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'publicacion_tablon'


class ComentarioTablon(models.Model):
    id_comentario = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_publicacion = models.ForeignKey(PublicacionTablon, on_delete=models.CASCADE, db_column='id_publicacion')
    id_cuenta = models.ForeignKey('usuarios.CuentaAcceso', on_delete=models.CASCADE, db_column='id_cuenta')
    mensaje = models.TextField()
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'comentario_tablon'


class RegistroAsistencia(models.Model):
    id_asistencia = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_alumno = models.ForeignKey('usuarios.Alumno', on_delete=models.CASCADE, db_column='id_alumno')
    id_curso = models.ForeignKey('academia.CursoMateria', on_delete=models.CASCADE, db_column='id_curso')
    id_estado_asistencia = models.ForeignKey(EstadoAsistencia, on_delete=models.PROTECT, db_column='id_estado_asistencia', null=True, blank=True)
    fecha_registro = models.DateField()
    justificacion_observacion = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'registro_asistencia'


class AlertaRiesgoIa(models.Model):
    id_alerta = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_alumno = models.ForeignKey('usuarios.Alumno', on_delete=models.CASCADE, db_column='id_alumno')
    id_nivel_riesgo = models.ForeignKey(NivelRiesgo, on_delete=models.PROTECT, db_column='id_nivel_riesgo', null=True, blank=True)
    id_estado_validacion = models.ForeignKey(EstadoValidacionAlerta, on_delete=models.PROTECT, db_column='id_estado_validacion', null=True, blank=True)
    motivo_alerta = models.TextField()
    
    # METRICAS NUMÉRICAS PARA DESBIASING
    metricas_disparadoras = models.JSONField(blank=True, null=True, help_text="Ej: {'inasistencias': 3, 'promedio': 5.2}")
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'alerta_riesgo_ia'


class SugerenciaIaSemanal(models.Model):
    id_sugerencia = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_cuenta = models.ForeignKey('usuarios.CuentaAcceso', on_delete=models.CASCADE, db_column='id_cuenta')
    mensaje_accionable = models.TextField()
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'sugerencia_ia_semanal'


class LogActividadUsuario(models.Model):
    id_log = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_cuenta = models.ForeignKey('usuarios.CuentaAcceso', on_delete=models.CASCADE, db_column='id_cuenta')
    ip_origen = models.GenericIPAddressField(blank=True, null=True)
    accion_realizada = models.TextField()
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'log_actividad_usuario'