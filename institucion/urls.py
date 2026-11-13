from django.urls import path
from django.contrib.auth.decorators import permission_required, login_required
from .views import (
    InstitucionListView, InstitucionDetailView, InstitucionCreateView, InstitucionUpdateView, InstitucionDeleteView,
    SedeListView, SedeDetailView, SedeCreateView, SedeUpdateView, SedeDeleteView,
    IntegracionSistemaListView, IntegracionSistemaDetailView, IntegracionSistemaCreateView, IntegracionSistemaUpdateView, IntegracionSistemaDeleteView,
    PasoOnboardingListView, PasoOnboardingDetailView, PasoOnboardingCreateView, PasoOnboardingUpdateView, PasoOnboardingDeleteView,
)

urlpatterns = [
    # --- INSTITUCION ---
    path('instituciones/', login_required(InstitucionListView.as_view()), name='institucion_list'),
    path('instituciones/<uuid:pk>/', login_required(InstitucionDetailView.as_view()), name='institucion_detail'),
    path('instituciones/create/', permission_required('institucion.add_institucion')(InstitucionCreateView.as_view()), name='institucion_create'),
    path('instituciones/<uuid:pk>/update/', permission_required('institucion.change_institucion')(InstitucionUpdateView.as_view()), name='institucion_update'),
    path('instituciones/<uuid:pk>/delete/', permission_required('institucion.delete_institucion')(InstitucionDeleteView.as_view()), name='institucion_delete'),

    # --- SEDE ---
    path('sedes/', login_required(SedeListView.as_view()), name='sede_list'),
    path('sedes/<uuid:pk>/', login_required(SedeDetailView.as_view()), name='sede_detail'),
    path('sedes/create/', permission_required('institucion.add_sede')(SedeCreateView.as_view()), name='sede_create'),
    path('sedes/<uuid:pk>/update/', permission_required('institucion.change_sede')(SedeUpdateView.as_view()), name='sede_update'),
    path('sedes/<uuid:pk>/delete/', permission_required('institucion.delete_sede')(SedeDeleteView.as_view()), name='sede_delete'),

    # --- INTEGRACION SISTEMA ---
    path('integraciones/', login_required(IntegracionSistemaListView.as_view()), name='integracionsistema_list'),
    path('integraciones/<uuid:pk>/', login_required(IntegracionSistemaDetailView.as_view()), name='integracionsistema_detail'),
    path('integraciones/create/', permission_required('institucion.add_integracionsistema')(IntegracionSistemaCreateView.as_view()), name='integracionsistema_create'),
    path('integraciones/<uuid:pk>/update/', permission_required('institucion.change_integracionsistema')(IntegracionSistemaUpdateView.as_view()), name='integracionsistema_update'),
    path('integraciones/<uuid:pk>/delete/', permission_required('institucion.delete_integracionsistema')(IntegracionSistemaDeleteView.as_view()), name='integracionsistema_delete'),

    # --- PASO ONBOARDING ---
    path('pasos-onboarding/', login_required(PasoOnboardingListView.as_view()), name='pasoonboarding_list'),
    path('pasos-onboarding/<uuid:pk>/', login_required(PasoOnboardingDetailView.as_view()), name='pasoonboarding_detail'),
    path('pasos-onboarding/create/', permission_required('institucion.add_pasoonboarding')(PasoOnboardingCreateView.as_view()), name='pasoonboarding_create'),
    path('pasos-onboarding/<uuid:pk>/update/', permission_required('institucion.change_pasoonboarding')(PasoOnboardingUpdateView.as_view()), name='pasoonboarding_update'),
    path('pasos-onboarding/<uuid:pk>/delete/', permission_required('institucion.delete_pasoonboarding')(PasoOnboardingDeleteView.as_view()), name='pasoonboarding_delete'),
]