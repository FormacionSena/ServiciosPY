from django import forms
from .models import Usuario, Servicio, AsignacionServicio

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'telefono']

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombre', 'categoria']

class AsignacionServicioForm(forms.ModelForm):
    class Meta:
        model = AsignacionServicio
        fields = ['usuario', 'servicio', 'estado']
