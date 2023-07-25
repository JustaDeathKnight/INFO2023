from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria, Articulo, Comentario
from django.contrib.auth.decorators import login_required
from apps.usuarios.models import Usuario
from .forms import ArticuloForm, ComentarioForm, CategoriaForm


# Create your views here.


def articulos_por_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id = categoria_id)
    articulos = Articulo.objects.filter(categoria_articulo = categoria)
    
    return render(request,'articulos/articulos_por_categoria.html', {'categoria':categoria, 'articulos': articulos})


@login_required
def AddArticulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST, request.FILES)
        try:
            if form.is_valid():
                print("Datos recibidos en el formulario:")
                print(request.POST)
                print("Datos del formulario validado:")
                print(form.cleaned_data)
                articulo = form.save(commit=False)
                articulo.autor = request.user  # Asignar el autor del artículo al usuario autenticado
                articulo.save()
                return redirect('home')
        except Exception as e:
            # Captura cualquier excepción y muestra un mensaje de error
            error_message = f"Ha ocurrido un problema al crear el artículo: {str(e)}"
            form.add_error(None, error_message)  # Añade el mensaje de error al formulario
    else:
        form = ArticuloForm()

    categorias = Categoria.objects.all()

    return render(request, 'articulos/add_articulo.html', {'form': form, 'categorias': categorias})

@login_required
def editar_articulo(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    
    if request.method == 'POST':
        form = ArticuloForm(request.POST, request.FILES, instance=articulo)
        if form.is_valid():
            form.save()
            return redirect('detalle_articulo', pk=pk)
    else:
        form = ArticuloForm(instance=articulo)
    
    return render(request, 'articulos/editar_articulo.html', {'form': form, 'articulo': articulo})

@login_required
def borrar_articulo(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    if request.method == 'POST':
        articulo.delete()
        return redirect('home')
    return render(request, 'articulos/borrar_articulo.html', {'articulo': articulo})


# def detalle_articulo(request, pk):
#     articulo = get_object_or_404(Articulo, pk=pk)

#     if request.method == 'POST':
#         form = ComentarioForm(request.POST)
#         if form.is_valid():
#             comentario = form.save(commit=False)
#             comentario.autor = request.user
#             comentario.save()
#             articulo.comentarios.add(comentario)
#             return redirect('detalle_articulo', pk=pk)
#     else:
#         form = ComentarioForm()

#     return render(request, 'articulos/detalle_articulo.html', {'articulo': articulo, 'form': form})

def detalle_articulo(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)

    if request.method == 'POST':
        # Comprobamos si se está enviando el formulario para agregar un nuevo comentario
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.autor = request.user
            comentario.save()
            articulo.comentarios.add(comentario)
            return redirect('detalle_articulo', pk=pk)
    else:
        form = ComentarioForm()

    # Si se incluye el comentario_id en la solicitud, significa que se quiere editar o borrar un comentario
    comentario_id = request.GET.get('comentario_id')
    if comentario_id:
        comentario = get_object_or_404(Comentario, id=comentario_id)

        # Verificar si el usuario que quiere editar o borrar el comentario es el autor del comentario o un administrador
        if request.user == comentario.autor or request.user.is_staff:
            if 'editar' in request.GET:
                # Modo de edición del comentario
                if request.method == 'POST':
                    form = ComentarioForm(request.POST, instance=comentario)
                    if form.is_valid():
                        form.save()
                        return redirect('detalle_articulo', pk=pk)
                else:
                    form = ComentarioForm(instance=comentario)
                return render(request, 'articulos/detalle_articulo.html', {'articulo': articulo, 'form': form, 'comentario_id': comentario_id})
            elif 'borrar' in request.GET:
                # Modo de borrado del comentario
                if request.method == 'POST':
                    comentario.delete()
                    return redirect('detalle_articulo', pk=pk)
                else:
                    return render(request, 'articulos/detalle_articulo.html', {'articulo': articulo, 'comentario_id': comentario_id})

    return render(request, 'articulos/detalle_articulo.html', {'articulo': articulo, 'form': form})

def agregar_comentario(request, articulo_id):
    articulo = get_object_or_404(Articulo, id=articulo_id)

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            contenido = form.cleaned_data['contenido']
            autor = request.user  # El usuario logueado será el autor del comentario
            comentario = Comentario.objects.create(autor=autor, contenido=contenido)
            articulo.comentarios.add(comentario)  # Usamos el método add() para agregar el comentario al artículo
            return redirect('detalle_articulo', pk=articulo.id)
    else:
        form = ComentarioForm()

    return render(request, 'agregar_comentario.html', {'form': form})

from django.shortcuts import get_object_or_404, redirect, render
from .models import Articulo, Comentario
from .forms import ComentarioForm
# ...

# @login_required
# def editar_comentario(request, pk, comentario_id):
#     articulo = get_object_or_404(Articulo, pk=pk)
#     comentario = get_object_or_404(Comentario, pk=comentario_id)

#     # Verificar si el usuario que quiere editar el comentario es el autor del comentario o un administrador
#     if request.user == comentario.autor or request.user.is_staff:
#         if request.method == 'POST':
#             form = ComentarioForm(request.POST, instance=comentario)
#             if form.is_valid():
#                 form.save()
#                 return redirect('detalle_articulo', pk=pk)
#         else:
#             form = ComentarioForm(instance=comentario)
#         return render(request, 'articulos/editar_comentario.html', {'form': form})
#     else:
#         # Aquí puedes manejar el caso en que el usuario no tenga permisos para editar el comentario
#         # Por ejemplo, puedes redirigirlo a otra página o mostrar un mensaje de error.
#         pass

#     return redirect('detalle_articulo', pk=pk)

# @login_required
# def borrar_comentario(request, pk, comentario_id):
#     articulo = get_object_or_404(Articulo, pk=pk)
#     comentario = get_object_or_404(Comentario, pk=comentario_id)

#     # Verificar si el usuario que quiere borrar el comentario es el autor del comentario o un administrador
#     if request.user == comentario.autor or request.user.is_staff:
#         comentario.delete()
#     else:
#         # Aquí puedes manejar el caso en que el usuario no tenga permisos para borrar el comentario
#         # Por ejemplo, puedes redirigirlo a otra página o mostrar un mensaje de error.
#         pass

#     return redirect('detalle_articulo', pk=pk)

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirige a la página principal o la que desees
    else:
        form = CategoriaForm()

    return render(request, 'articulos/crear_categoria.html', {'form': form})
