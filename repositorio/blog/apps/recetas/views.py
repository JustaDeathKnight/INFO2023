from django.shortcuts import render
from .models import Recetas, Categoria
from django.views.generic.list import ListView #para las vistas con class
# Create your views here.
def ListarRecetas(request):
    contexto = {}
    id_categoria = request.GET.get("id", None)
    if id_categoria:
        n = Recetas.objects.filter(categoria_receta = id_categoria)
    else:
        n = Recetas.objects.all() # es para que nos traiga todas las recetas que tengamos

    contexto['Recetas'] = n

    cat = Categoria.objects.all().order_by('nombre') #ordena la categoria por nombre
    contexto['categorias'] = cat

    return render(request, 'recetas/listar.html', contexto) 

def DetalleReceta(request, pk):
    contexto = {}

    n = Recetas.objects.get(pk = pk) # para que nos traiga solamente la receta que se elija

    contexto['Receta'] = n

    return render(request, 'recetas/detalle.html', contexto)

 

