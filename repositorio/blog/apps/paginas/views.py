from django.shortcuts import render
from apps.articulos.models import Articulo, Categoria

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
