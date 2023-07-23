from django.urls import path
from . import views

urlpatterns = [
    path('categorias/<int:categoria_id>/', views.articulos_por_categoria, name='articulos_por_categoria'),
    path('articulo/<int:pk>/', views.detalle_articulo, name='detalle_articulo'),
    path('add_articulo', views.AddArticulo, name='add_articulo'),
    path('articulo/<int:pk>/editar/', views.editar_articulo, name='editar_articulo'),
    path('articulo/<int:pk>/borrar/', views.borrar_articulo, name='borrar_articulo'),
    path('articulo/<int:articulo_id>/editar-comentario/<int:comentario_id>/', views.editar_comentario, name='editar_comentario'),
    path('articulo/<int:articulo_id>/borrar-comentario/<int:comentario_id>/', views.borrar_comentario, name='borrar_comentario'),

]
