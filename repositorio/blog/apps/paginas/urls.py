from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('categorias/', views.categorias, name='categorias'),
    path('acerca_de/', views.acerca_de, name='acerca_de'),  
    path('contacto/', views.contacto, name='contacto'),
]

