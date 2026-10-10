from django.contrib import admin
from .models import Institucion, Sede, IntegracionSistema, PasoOnboarding

@admin.register(Institucion)
class InstitucionAdmin(admin.ModelAdmin):
    list_display = ('nombre_institucion', 'clave_cct_rvoe', 'email_contacto', 'creado_en')
    search_fields = ('nombre_institucion', 'clave_cct_rvoe', 'rfc_identificador_fiscal')

@admin.register(Sede)
class SedeAdmin(admin.ModelAdmin):
    list_display = ('nombre_sede', 'id_institucion', 'ciudad', 'estado_provincia', 'pais')
    list_filter = ('id_institucion', 'estado_provincia')
    search_fields = ('nombre_sede', 'codigo_campus')

@admin.register(IntegracionSistema)
class IntegracionSistemaAdmin(admin.ModelAdmin):
    list_display = ('tipo_sistema', 'id_institucion', 'estado_conexion', 'ultima_sincronizacion')
    list_filter = ('estado_conexion', 'tipo_sistema')

@admin.register(PasoOnboarding)
class PasoOnboardingAdmin(admin.ModelAdmin):
    list_display = ('nombre_paso', 'id_institucion', 'orden_secuencia', 'estado_paso')
    list_filter = ('estado_paso',)