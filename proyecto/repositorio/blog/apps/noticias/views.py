from django.shortcuts import render
from .models import Noticia

# Create your views here.


def ListarNoticias(request):
    contexto = { }
    
    n = Noticia.objects.all() # select * from noticias_noticias
    
    contexto['noticias'] = n
    
    return render(request, 'noticias/listar.html', contexto)

def DetalleNoticia(request, pk):
    contexto = { }
    
    n = Noticia.objects.get(pk=pk) # select * from noticias_noticias where id = id
    
    contexto['noticia'] = n
    
    return render(request, 'noticias/detalle.html', contexto)
