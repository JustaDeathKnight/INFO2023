from django.shortcuts import render
from apps.articulos.models import Articulo, Categoria
from django.db.models import Q
from django.utils import timezone

# Create your views here.
def home(request):
    return render(request, 'paginas/home.html')

def acerca_de(request):
    return render(request, 'paginas/acerca_de.html')

def contacto(request):
    return render(request, 'paginas/contacto.html')

def categorias(request):
    
    articulos = Articulo.objects.all()

    context = {
        'articulos': articulos,
        'categorias': Categoria.objects.all(),  
    }
    
    return render(request, 'paginas/categorias.html', context)

def articulos_all(request):
    categorias = Categoria.objects.all()
    articulos = Articulo.objects.all()
    orden = request.GET.get('orden')
    direccion = request.GET.get('direccion')

    # Obtener el valor del parámetro 'categoria' en la URL
    categoria_id = request.GET.get('categoria')
    if categoria_id:
        # Filtrar los artículos por la categoría seleccionada
        articulos = articulos.filter(categoria_articulo=categoria_id)

    # Obtener el valor del parámetro 'orden' en la URL
    if orden == 'titulo':
        articulos = articulos.order_by('titulo')
    elif orden == 'fecha_publicacion':
        articulos = articulos.order_by('fecha_publicacion')

    if direccion == 'desc':
        articulos = articulos.reverse()

    context = {
        'categorias': categorias,
        'articulos': articulos,
    }
    return render(request, 'paginas/articulos_all.html', context, )
