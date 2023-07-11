from django.shortcuts import get_object_or_404, render, redirect, reverse
from .models import Noticia, Categoria
from .forms import ComentarioForm, NoticiaForm

# Create your views here.


def ListarNoticias(request):
    contexto = { } # diccionario
    id_categoria = request.GET.get('id', None)
    
    if id_categoria:
        n = Noticia.objects.filter(categoria_noticia = id_categoria)
    else:
        n = Noticia.objects.all() # select * from noticias_noticias
    
    contexto['noticias'] = n
    
    cat = Categoria.objects.all().order_by('nombre') # Ordena por nombre
    contexto['categorias'] = cat
    
    return render(request, 'noticias/listar.html', contexto)

def DetalleNoticia(request, pk):
    contexto = { }
    
    n = Noticia.objects.get(pk=pk) # select * from noticias_noticias where id = id
    
    contexto['noticia'] = n
    
    return render(request, 'noticias/detalle.html', contexto)

def add_noticia(request):
    form = NoticiaForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect(reverse('home'))
    
    return render(request, 'noticias/addNoticia.html', {'form': form})

def add_comentario(request, pk):
    
    noticia = get_object_or_404(Noticia, pk=pk)    
    form = ComentarioForm(request.POST or None)
    
    if form.is_valid():
        comentario = form.save(commit=False)
        comentario.noticias = noticia
        comentario.save()
        return redirect(reverse('noticias:detalle', args=[pk]))