from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('articulos/', views.articulos_all, name='articulos'),
    path('categorias/', views.categorias, name='categorias'),
    path('acerca_de/', views.acerca_de, name='acerca_de'),  
    path('contacto/', views.contacto, name='contacto'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

