from django.urls import path
from . import views

urlpatterns = [
    path('categorias/<int:categoria_id>/', views.articulos_por_categoria, name='articulos_por_categoria'),
    path('articulo/<int:articulo_id>/', views.detalle_articulo, name='detalle_articulo'),
    path('add_articulo', views.AddArticulo, name='add_articulo'),
    path('borrar_articulo/<int:pk>/', views.borrar_articulo, name='borrar_articulo'),
]
