from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Institucion, Sede, IntegracionSistema, PasoOnboarding

# --- INSTITUCION ---
class InstitucionListView(ListView):
    model = Institucion

class InstitucionDetailView(DetailView):
    model = Institucion

class InstitucionCreateView(CreateView):
    model = Institucion
    fields = [
        'nombre_institucion', 'clave_cct_rvoe', 'razon_social',
        'rfc_identificador_fiscal', 'direccion_fiscal', 'telefono_contacto',
        'email_contacto', 'logo_url', 'sitio_web'
    ]
    template_name = 'institucion/nuevo_institucion.html'
    success_url = '/institucion/instituciones/'

class InstitucionUpdateView(UpdateView):
    model = Institucion
    fields = [
        'nombre_institucion', 'clave_cct_rvoe', 'razon_social',
        'rfc_identificador_fiscal', 'direccion_fiscal', 'telefono_contacto',
        'email_contacto', 'logo_url', 'sitio_web'
    ]
    template_name = 'institucion/editar_institucion.html'
    success_url = '/institucion/instituciones/'

class InstitucionDeleteView(DeleteView):
    model = Institucion
    success_url = '/institucion/instituciones/'


# --- SEDE ---
class SedeListView(ListView):
    model = Sede

class SedeDetailView(DetailView):
    model = Sede

class SedeCreateView(CreateView):
    model = Sede
    fields = [
        'id_institucion', 'nombre_sede', 'codigo_campus', 'direccion_calle',
        'ciudad', 'estado_provincia', 'codigo_postal', 'pais',
        'telefono_responsable', 'email_responsable'
    ]
    template_name = 'institucion/nuevo_sede.html'
    success_url = '/institucion/sedes/'

class SedeUpdateView(UpdateView):
    model = Sede
    fields = [
        'id_institucion', 'nombre_sede', 'codigo_campus', 'direccion_calle',
        'ciudad', 'estado_provincia', 'codigo_postal', 'pais',
        'telefono_responsable', 'email_responsable'
    ]
    template_name = 'institucion/editar_sede.html'
    success_url = '/institucion/sedes/'

class SedeDeleteView(DeleteView):
    model = Sede
    success_url = '/institucion/sedes/'


# --- INTEGRACION SISTEMA ---
class IntegracionSistemaListView(ListView):
    model = IntegracionSistema

class IntegracionSistemaDetailView(DetailView):
    model = IntegracionSistema

class IntegracionSistemaCreateView(CreateView):
    model = IntegracionSistema
    fields = ['id_institucion', 'tipo_sistema', 'credenciales_api_key', 'url_endpoint', 'estado_conexion', 'ultima_sincronizacion']
    template_name = 'institucion/nuevo_integracion.html'
    success_url = '/institucion/integraciones/'

class IntegracionSistemaUpdateView(UpdateView):
    model = IntegracionSistema
    fields = ['id_institucion', 'tipo_sistema', 'credenciales_api_key', 'url_endpoint', 'estado_conexion', 'ultima_sincronizacion']
    template_name = 'institucion/editar_integracion.html'
    success_url = '/institucion/integraciones/'

class IntegracionSistemaDeleteView(DeleteView):
    model = IntegracionSistema
    success_url = '/institucion/integraciones/'


# --- PASO ONBOARDING ---
class PasoOnboardingListView(ListView):
    model = PasoOnboarding

class PasoOnboardingDetailView(DetailView):
    model = PasoOnboarding

class PasoOnboardingCreateView(CreateView):
    model = PasoOnboarding
    fields = ['id_institucion', 'nombre_paso', 'descripcion', 'orden_secuencia', 'estado_paso', 'completado_en']
    template_name = 'institucion/nuevo_paso_onboarding.html'
    success_url = '/institucion/pasos-onboarding/'

class PasoOnboardingUpdateView(UpdateView):
    model = PasoOnboarding
    fields = ['id_institucion', 'nombre_paso', 'descripcion', 'orden_secuencia', 'estado_paso', 'completado_en']
    template_name = 'institucion/editar_paso_onboarding.html'
    success_url = '/institucion/pasos-onboarding/'

class PasoOnboardingDeleteView(DeleteView):
    model = PasoOnboarding
    success_url = '/institucion/pasos-onboarding/'