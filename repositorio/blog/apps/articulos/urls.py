from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('categorias/<int:categoria_id>/', views.articulos_por_categoria, name='articulos_por_categoria'),
    # path('articulo/<int:pk>/', views.detalle_articulo, name='detalle_articulo'),
    path('add_articulo', views.AddArticulo, name='add_articulo'),
    path('articulo/<int:pk>/editar/', views.editar_articulo, name='editar_articulo'),
    path('articulo/<int:pk>/borrar/', views.borrar_articulo, name='borrar_articulo'),
    path('articulo/<int:pk>/detalle/', views.detalle_articulo, name='detalle_articulo'),
    # path('articulo/<int:pk>/borrar-comentario/<int:comentario_id>/', views.borrar_comentario, name='borrar_comentario'),
    # path('articulo/<int:pk>/editar-comentario/<int:comentario_id>/', views.editar_comentario, name='editar_comentario'),
    path('crear_categoria/', views.crear_categoria, name='crear_categoria'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
