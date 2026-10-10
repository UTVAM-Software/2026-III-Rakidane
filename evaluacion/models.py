import uuid
from django.db import models

# --- CATÁLOGOS REUTILIZABLES ---
class EstadoEntrega(models.Model):
    id_estado_entrega = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre_estado = models.CharField(max_length=50, unique=True, help_text="Pendiente, Entregado, Entregado con Retraso, No Entregado")

    class Meta:
        db_table = 'estado_entrega'

    def __str__(self):
        return self.nombre_estado


class EstadoRevision(models.Model):
    id_estado_revision = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre_estado = models.CharField(max_length=50, unique=True, help_text="Sin Revisar, Pre-evaluado por IA, Revisado por Docente")

    class Meta:
        db_table = 'estado_revision'

    def __str__(self):
        return self.nombre_estado


# --- TABLAS PRINCIPALES ---
class RubricaEvaluacion(models.Model):
    id_rubrica = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_leccion = models.ForeignKey('academia.LeccionActividad', on_delete=models.CASCADE, db_column='id_leccion', null=True, blank=True)
    nombre_rubrica = models.CharField(max_length=150)
    descripcion_general = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'rubrica_evaluacion'

    def __str__(self):
        return self.nombre_rubrica


class CriterioRubrica(models.Model):
    id_criterio = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_rubrica = models.ForeignKey(RubricaEvaluacion, on_delete=models.CASCADE, db_column='id_rubrica')
    nombre_criterio = models.CharField(max_length=100)
    descripcion_criterio = models.TextField(blank=True, null=True)
    puntaje_maximo = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table = 'criterio_rubrica'

    def __str__(self):
        return f"{self.nombre_criterio} ({self.puntaje_maximo} pts)"


class EntregaTarea(models.Model):
    id_entrega = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_leccion = models.ForeignKey('academia.LeccionActividad', on_delete=models.CASCADE, db_column='id_leccion')
    id_alumno = models.ForeignKey('usuarios.Alumno', on_delete=models.CASCADE, db_column='id_alumno')
    id_estado_entrega = models.ForeignKey(EstadoEntrega, on_delete=models.PROTECT, db_column='id_estado_entrega', null=True, blank=True)
    id_estado_revision = models.ForeignKey(EstadoRevision, on_delete=models.PROTECT, db_column='id_estado_revision', null=True, blank=True)
    texto_contenido = models.TextField(blank=True, null=True)
    fecha_envio = models.DateTimeField(auto_now_add=True)
    calificacion_final = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    retroalimentacion_docente = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'entrega_tarea'


class ArchivoEntrega(models.Model):
    id_archivo = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_entrega = models.ForeignKey(EntregaTarea, on_delete=models.CASCADE, db_column='id_entrega')
    nombre_original = models.CharField(max_length=200, blank=True, null=True)
    ruta_almacenamiento = models.TextField()

    class Meta:
        db_table = 'archivo_entrega'


class EvaluacionIaBorrador(models.Model):
    id_eval_ia = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_entrega = models.OneToOneField(EntregaTarea, on_delete=models.CASCADE, db_column='id_entrega')
    modelo_ia_utilizado = models.CharField(max_length=50, default='gpt-4o')
    puntaje_sugerido = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    porcentaje_confianza = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    comentario_general = models.TextField(blank=True, null=True)
    prompt_utilizado = models.TextField(blank=True, null=True)
    
    # AUDITORÍA DE SESGOS DE IA
    datos_origen_json = models.JSONField(blank=True, null=True, help_text="Payload/Contexto exacto enviado al LLM")
    fue_modificado_por_docente = models.BooleanField(default=False)
    puntaje_final_docente = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'evaluacion_ia_borrador'


class EvaluacionCriterioDetalle(models.Model):
    id_eval_criterio = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_eval_ia = models.ForeignKey(EvaluacionIaBorrador, on_delete=models.CASCADE, db_column='id_eval_ia')
    id_criterio = models.ForeignKey(CriterioRubrica, on_delete=models.CASCADE, db_column='id_criterio')
    puntaje_criterio = models.DecimalField(max_digits=5, decimal_places=2)
    evidencia_citada = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'evaluacion_criterio_detalle'


class BoletaCalificacion(models.Model):
    id_boleta = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_inscripcion = models.OneToOneField('academia.InscripcionCurso', on_delete=models.CASCADE, db_column='id_inscripcion')
    parcial_1 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    parcial_2 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    parcial_3 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    promedio_final = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    observaciones = models.TextField(blank=True, null=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'boleta_calificacion'