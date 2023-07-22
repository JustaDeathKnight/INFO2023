from django.urls import include, path
from . import views  # Importamos las vistas de la aplicación

app_name='recetas'

urlpatterns = [
    # estructura de la ruta:
    # path('ruta', views.vista_a_ejecutar, name='nombre_ruta')
    # Ruta para la vista Home
    path('', views.ListarRecetas, name='listar'),
    path('detalle/<int:pk>', views.DetalleReceta, name = 'detalle'),
   
    
]