from django.shortcuts import render
from .models import Recetas
# Create your views here.
def ListarRecetas(request):
    contexto = {}

    n = Recetas.objects.all() # es para que nos traiga todas las recetas que tengamos

    contexto['Recetas'] = n

    return render(request, 'recetas/listar.html', contexto) 

def DetalleReceta(request, pk):
    contexto = {}

    n = Recetas.objects.get(pk = pk) # para que nos traiga solamente la receta que se elija

    contexto['Receta'] = n

    return render(request, 'recetas/detalle.html', contexto) 
