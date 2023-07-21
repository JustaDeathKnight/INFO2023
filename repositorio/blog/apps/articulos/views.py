from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria, Articulo

# Create your views here.


def articulos_por_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id = categoria_id)
    articulos = Articulo.objects.filter(categoria_articulo = categoria)
    return render(request,'articulos/articulos_por_categoria.html', {'categoria':categoria, 'articulos': articulos})

def detalle_articulo(request, articulo_id):
    articulo = get_object_or_404(Articulo, id=articulo_id)
    return render(request, 'articulos/detalle_articulo.html', {'articulo': articulo})