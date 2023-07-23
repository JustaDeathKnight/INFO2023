from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import CreateView
from .forms import RegistroForm, ColabForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse_lazy

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username') # username es el name del input del formulario
        password = request.POST.get('password') # password es el name del input del formulario
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Usuario o contraseña no validos')
    return render(request, 'usuarios/login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

def user_register(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario creado correctamente')
            return redirect('login')
        else:
            messages.error(request, 'Error al crear el usuario')
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})

# Verifica si el usuario es superusuario
@user_passes_test(lambda u: u.is_superuser)
def user_colab(request):
    if request.method == 'POST':
        form = ColabForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario creado correctamente')
            return redirect('login')
        else:
            messages.error(request, 'Error al crear el usuario')
    else:
        form = ColabForm()
    return render(request, 'usuarios/colaborador.html', {'form': form})