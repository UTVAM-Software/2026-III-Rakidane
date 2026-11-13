from django import forms
from django.contrib.auth.models import User
from .models import CuentaAcceso, RolCuenta

class RegistroPublicoForm(forms.ModelForm):
    email = forms.EmailField(
        label="Correo Electrónico",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'correo@utvam.edu.mx'})
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '••••••••'})
    )
    rol_solicitado = forms.ModelChoiceField(
        queryset=RolCuenta.objects.all(),
        label="Rol que solicitas",
        widget=forms.Select(attrs={'class': 'form-select'}),
        empty_label="-- Selecciona un Rol --"
    )

    class Meta:
        model = User
        fields = ['email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        # Asignamos el correo tanto a username como a email
        user.username = self.cleaned_data["email"]
        user.email = self.cleaned_data["email"]
        user.set_password(self.cleaned_data["password"])
        user.is_active = False  # 🔒 Se guarda inactivo hasta aprobación del admin
        
        if commit:
            user.save()
            rol = self.cleaned_data["rol_solicitado"]
            CuentaAcceso.objects.create(
                email=user.email,
                id_rol=rol,
                esta_activo=False
            )
        return user