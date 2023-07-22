from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria, Articulo
from django.contrib.auth.decorators import login_required
from apps.usuarios.models import Usuario
from .forms import ArticuloForm


# Create your views here.


def articulos_por_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id = categoria_id)
    articulos = Articulo.objects.filter(categoria_articulo = categoria)
    
    return render(request,'articulos/articulos_por_categoria.html', {'categoria':categoria, 'articulos': articulos})

def detalle_articulo(request, articulo_id):
    articulo = get_object_or_404(Articulo, id=articulo_id)
    return render(request, 'articulos/detalle_articulo.html', {'articulo': articulo})

@login_required
def AddArticulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST, request.FILES) ##REQUEST FILE PARA LAS IMAGENES
        if form.is_valid():
            articulo = form.save(commit=False)
            articulo.author = request.user #autor de la noticia
            articulo.save()
            return redirect('home')
    else:
        form = ArticuloForm()
    
    categorias = Categoria.objects.all()
    
    return render(request, 'articulos/add_articulo.html', {'form': form, 'categorias': categorias})

@login_required
def borrar_articulo(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    if request.method == 'POST':
        articulo.delete()
        return redirect('home')
    return render(request, 'articulos/borrar_articulo.html', {'articulo': articulo})