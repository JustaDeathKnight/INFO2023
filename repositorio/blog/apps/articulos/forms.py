from django import forms
from .models import Articulo, Comentario, Categoria


class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['titulo', 'resumen', 'contenido',
                  'imagen', 'categoria_articulo']


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']
        exclude = ['autor']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ComentarioForm, self).__init__(*args, **kwargs)
        if user:
            self.instance.autor = user.username


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'icono']
