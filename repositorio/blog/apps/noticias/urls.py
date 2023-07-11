from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'noticias'

urlpatterns = [
    path('', views.ListarNoticias, name='listar'),

    path('listarNoticias/', views.ListarNoticias, name='listar'),

    path('detalle/<int:pk>/', views.DetalleNoticia, name='detalle'),

    path('addNoticia', views.add_noticia, name='addNoticia')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
