from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria, Articulo, Comentario
from django.contrib.auth.decorators import login_required, user_passes_test
from apps.usuarios.models import Usuario
from .forms import ArticuloForm, ComentarioForm, CategoriaForm


# Create your views here.
# Restricción para las vistas que solo pueden ser accedidas por colaboradores y superusuarios
# def es_colaborador_o_superuser(user):
#     return user.is_authenticated and (user.is_colaborador or user.is_superuser)


def articulos_por_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    articulos = Articulo.objects.filter(categoria_articulo=categoria)

    return render(request, 'articulos/articulos_por_categoria.html', {'categoria': categoria, 'articulos': articulos})


@login_required
# @user_passes_test(es_colaborador_o_superuser)
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
                return redirect('articulos')
        except Exception as e:
            # Captura cualquier excepción y muestra un mensaje de error
            error_message = f"Ha ocurrido un problema al crear el artículo: {str(e)}"
            # Añade el mensaje de error al formulario
            form.add_error(None, error_message)
    else:
        form = ArticuloForm()

    categorias = Categoria.objects.all()

    return render(request, 'articulos/add_articulo.html', {'form': form, 'categorias': categorias})


@login_required
# @user_passes_test(es_colaborador_o_superuser)
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
# @user_passes_test(es_colaborador_o_superuser)
def borrar_articulo(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    if request.method == 'POST':
        articulo.delete()
        return redirect('articulos')
    return render(request, 'articulos/borrar_articulo.html', {'articulo': articulo})


def detalle_articulo(request, pk):

    articulo = get_object_or_404(Articulo, id=pk)

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            contenido = form.cleaned_data['contenido']
            autor = request.user  # El usuario logueado será el autor del comentario
            comentario = Comentario.objects.create(
                autor=autor, contenido=contenido)
            # Usamos el método add() para agregar el comentario al artículo
            articulo.comentarios.add(comentario)
            return redirect('detalle_articulo', pk=articulo.id)
    else:
        form = ComentarioForm()

    return render(request, 'articulos/detalle_articulo.html', {'articulo': articulo, 'form': form})


@login_required
def agregar_comentario(request, articulo_id):
    articulo = get_object_or_404(Articulo, id=articulo_id)

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            contenido = form.cleaned_data['contenido']
            autor = request.user  # El usuario logueado será el autor del comentario
            comentario = Comentario.objects.create(
                autor=autor, contenido=contenido)
            # Usamos el método add() para agregar el comentario al artículo
            articulo.comentarios.add(comentario)
            return redirect('detalle_articulo', pk=articulo.id)
    else:
        form = ComentarioForm()

    return render(request, 'agregar_comentario.html', {'form': form})


@login_required
def borrar_comentario(request, pk, comentario_id):
    articulo = get_object_or_404(Articulo, id=pk)
    comentario = get_object_or_404(Comentario, id=comentario_id)
    if comentario.autor or comentario.is_staff or request.user.is_colaborador:
        if request.method == 'POST':
            comentario.delete()
            return redirect('detalle_articulo', pk=articulo.id)
    return render(request, 'articulos/borrar_comentario.html', {'comentario': comentario, 'articulo': articulo})


@login_required
def editar_comentario(request, pk, comentario_id):
    articulo = get_object_or_404(Articulo, id=pk)
    comentario = get_object_or_404(Comentario, id=comentario_id)
    if comentario.autor or comentario.is_staff or request.user.is_colaborador:
        if request.method == 'POST':
            form = ComentarioForm(request.POST, instance=comentario)
            if form.is_valid():
                form.save()
                return redirect('detalle_articulo', pk=articulo.id)
        else:
            form = ComentarioForm(instance=comentario)
        return render(request, 'articulos/editar_comentario.html', {'form': form, 'comentario': comentario})


@login_required
# @user_passes_test(es_colaborador_o_superuser)
def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirige a la página principal o la que desees
            return redirect('home')
    else:
        form = CategoriaForm()

    return render(request, 'articulos/crear_categoria.html', {'form': form})
