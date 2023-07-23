from django import forms
from .models import Articulo, Comentario

class ArticuloForm(forms.ModelForm):
    
    class Meta:
        model = Articulo
        fields = ['titulo', 'resumen', 'contenido', 'imagen', 'categoria_articulo']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']