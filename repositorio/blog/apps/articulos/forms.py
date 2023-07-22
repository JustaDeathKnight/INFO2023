from django import forms
from .models import Articulo

class ArticuloForm(forms.ModelForm):
    
    class Meta:
        model = Articulo
        fields = ['titulo', 'resumen', 'contenido', 'imagen', 'categoria_articulo']





# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['text'] #campos de mi formulario
#         exclude = ['author']
    
#     def __init__(self, *args, **kwargs):
#         user = kwargs.pop('user', None)
#         super(CommentForm, self).__init__(*args, **kwargs)
#         if user:
#             self.instance.author = user.username