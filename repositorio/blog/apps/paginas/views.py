from django.shortcuts import render, redirect, get_object_or_404
from apps.articulos.models import Articulo, Categoria
import random
from .models import MensajeContacto
from .forms import FormularioContacto
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    categorias = Categoria.objects.all().order_by('nombre')

    # Obtener todos los artículos
    
    articulos = Articulo.objects.all()

    # Obtener 3 artículos aleatorios
    # Obtener 3 artículos aleatorios
    if articulos.count() >= 3:
        articulos_aleatorios = random.sample(list(articulos), 3)
    else:
        articulos_aleatorios = articulos
    # Otros procesamientos y lógicas...

    return render(request, 'paginas/home.html', {'categorias': categorias, 'articulos_aleatorios': articulos_aleatorios})


def acerca_de(request):
    return render(request, 'paginas/acerca_de.html')


def contacto(request):
    if request.method == 'POST':
        formulario = FormularioContacto(request.POST)
        if formulario.is_valid():
            # Procesar el formulario y guardar el mensaje
            nombre = formulario.cleaned_data['nombre']
            email = formulario.cleaned_data['email']
            mensaje = formulario.cleaned_data['mensaje']

            MensajeContacto.objects.create(
                nombre=nombre, email=email, mensaje=mensaje)

            # Redireccionar a una página de éxito o mostrar un mensaje de agradecimiento
            return redirect('home')
    else:
        formulario = FormularioContacto()

    return render(request, 'paginas/contacto.html', {'formulario': formulario})


def categorias(request):

    articulos = Articulo.objects.all()

    context = {
        'articulos': articulos,
        'categorias': Categoria.objects.all().order_by('nombre'),
    }

    return render(request, 'paginas/categorias.html', context)


def articulos_all(request):
    categorias = Categoria.objects.all().order_by('nombre')
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


@login_required
def ver_mensajes(request):
    mensajes = MensajeContacto.objects.all()
    return render(request, 'paginas/ver_mensajes.html', {'mensajes': mensajes})


@login_required
def borrar_mensaje(request, mensaje_id):
    mensaje = get_object_or_404(MensajeContacto, pk=mensaje_id)
    if request.method == 'POST':
        mensaje.delete()
        return redirect('ver_mensajes')
    return render(request, 'paginas/borrar_mensajes.html', {'mensaje': mensaje})
