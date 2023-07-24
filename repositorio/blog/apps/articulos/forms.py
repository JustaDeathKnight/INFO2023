from django import forms
from .models import Articulo, Comentario, Categoria

class ArticuloForm(forms.ModelForm):
    
    class Meta:
        model = Articulo
        fields = ['titulo', 'resumen', 'contenido', 'imagen', 'categoria_articulo']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'icono']