from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria, Articulo, Comentario
from django.contrib.auth.decorators import login_required
from apps.usuarios.models import Usuario
from .forms import ArticuloForm, ComentarioForm


# Create your views here.


def articulos_por_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id = categoria_id)
    articulos = Articulo.objects.filter(categoria_articulo = categoria)
    
    return render(request,'articulos/articulos_por_categoria.html', {'categoria':categoria, 'articulos': articulos})


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


def detalle_articulo(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    comentarios = articulo.comentarios.all()
    form = ComentarioForm()

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.autor = request.user
            comentario.save()
            articulo.comentarios.add(comentario)  # Agrega el comentario al artículo
            return redirect('detalle_articulo', pk=pk)

    return render(request, 'articulos/detalle_articulo.html', {'articulo': articulo, 'comentarios': comentarios, 'form': form})
