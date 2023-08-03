from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario


class RegistroForm(UserCreationForm):
    email = forms.EmailField(label='Correo', required=True)
    first_name = forms.CharField(label='Nombre', required=True)
    last_name = forms.CharField(label='Apellido', required=True)
    password1 = forms.CharField(
        label='Contraseña', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(
        label='Confirmar Contraseña', widget=forms.PasswordInput, required=True)

    class Meta:
        model = Usuario
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
        ]


class ColabForm(UserCreationForm):
    email = forms.EmailField(label='Correo', required=True)
    first_name = forms.CharField(label='Nombre', required=True)
    last_name = forms.CharField(label='Apellido', required=True)
    password1 = forms.CharField(
        label='Contraseña', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(
        label='Confirmar Contraseña', widget=forms.PasswordInput, required=True)
    is_colaborador = forms.BooleanField(
        label='Colaborador', widget=forms.CheckboxInput, required=False)

    class Meta:
        model = Usuario
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
            'is_colaborador'
        ]


class CambiarImagenForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'imagen'
        ]

    def __init__(self, *args, **kwargs):
        super(CambiarImagenForm, self).__init__(*args, **kwargs)
        self.fields['imagen'].required = True

    def clean_imagen(self):
        imagen = self.cleaned_data.get('imagen')
        if imagen:
            if imagen.size > 1024*1024*2:
                raise forms.ValidationError('La imagen no puede pesar más de 2MB')
            return imagen
        else:
            raise forms.ValidationError('No se ha podido leer la imagen')
