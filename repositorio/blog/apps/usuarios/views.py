from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import RegistroForm


# Create your views here.


def user_login(request):
    if request.method == 'POST':
        # Obtenemos los datos del formulario
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Autenticamos el usuario
        user = authenticate(request, username=username, password=password)

        # Si existe el usuario
        if user is not None:
            # Hacemos el login manualmente
            login(request, user)

            # Redireccionamos al home
            return redirect('home')
        else:
            # Si no existe el usuario mandamos un mensaje de error
            messages.error(request, 'Usuario o contraseña no validos')
    return render(request, 'usuarios/login.html')


def user_logout(request):
    # Hacemos el logout manualmente
    logout(request)

    # Redireccionamos al login
    return redirect('login')


class Registro(CreateView):
    # Formulario django
    form_class = RegistroForm
    success_url = reverse_lazy('login')
    template_name = 'usuarios/registro.html'