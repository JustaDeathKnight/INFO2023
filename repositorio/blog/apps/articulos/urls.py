from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('categorias/<int:categoria_id>/', views.articulos_por_categoria, name='articulos_por_categoria'),
    path('add_articulo', views.AddArticulo, name='add_articulo'),
    path('articulo/<int:pk>/editar/', views.editar_articulo, name='editar_articulo'),
    path('articulo/<int:pk>/borrar/', views.borrar_articulo, name='borrar_articulo'),
    path('articulo/<int:pk>/detalle/', views.detalle_articulo, name='detalle_articulo'),
    path('crear_categoria/', views.crear_categoria, name='crear_categoria'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
