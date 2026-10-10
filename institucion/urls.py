from django.urls import path
from .views import (
    InstitucionListView, InstitucionDetailView, InstitucionCreateView, InstitucionUpdateView, InstitucionDeleteView,
    SedeListView, SedeDetailView, SedeCreateView, SedeUpdateView, SedeDeleteView,
    IntegracionSistemaListView, IntegracionSistemaDetailView, IntegracionSistemaCreateView, IntegracionSistemaUpdateView, IntegracionSistemaDeleteView,
    PasoOnboardingListView, PasoOnboardingDetailView, PasoOnboardingCreateView, PasoOnboardingUpdateView, PasoOnboardingDeleteView,
)

urlpatterns = [
    # Institucion
    path('instituciones/', InstitucionListView.as_view(), name='institucion_list'),
    path('instituciones/<uuid:pk>/', InstitucionDetailView.as_view(), name='institucion_detail'),
    path('instituciones/create/', InstitucionCreateView.as_view(), name='institucion_create'),
    path('instituciones/<uuid:pk>/update/', InstitucionUpdateView.as_view(), name='institucion_update'),
    path('instituciones/<uuid:pk>/delete/', InstitucionDeleteView.as_view(), name='institucion_delete'),

    # Sede
    path('sedes/', SedeListView.as_view(), name='sede_list'),
    path('sedes/<uuid:pk>/', SedeDetailView.as_view(), name='sede_detail'),
    path('sedes/create/', SedeCreateView.as_view(), name='sede_create'),
    path('sedes/<uuid:pk>/update/', SedeUpdateView.as_view(), name='sede_update'),
    path('sedes/<uuid:pk>/delete/', SedeDeleteView.as_view(), name='sede_delete'),

    # IntegracionSistema
    path('integraciones/', IntegracionSistemaListView.as_view(), name='integracionsistema_list'),
    path('integraciones/<uuid:pk>/', IntegracionSistemaDetailView.as_view(), name='integracionsistema_detail'),
    path('integraciones/create/', IntegracionSistemaCreateView.as_view(), name='integracionsistema_create'),
    path('integraciones/<uuid:pk>/update/', IntegracionSistemaUpdateView.as_view(), name='integracionsistema_update'),
    path('integraciones/<uuid:pk>/delete/', IntegracionSistemaDeleteView.as_view(), name='integracionsistema_delete'),

    # PasoOnboarding
    path('pasos-onboarding/', PasoOnboardingListView.as_view(), name='pasoonboarding_list'),
    path('pasos-onboarding/<uuid:pk>/', PasoOnboardingDetailView.as_view(), name='pasoonboarding_detail'),
    path('pasos-onboarding/create/', PasoOnboardingCreateView.as_view(), name='pasoonboarding_create'),
    path('pasos-onboarding/<uuid:pk>/update/', PasoOnboardingUpdateView.as_view(), name='pasoonboarding_update'),
    path('pasos-onboarding/<uuid:pk>/delete/', PasoOnboardingDeleteView.as_view(), name='pasoonboarding_delete'),
]