from django.db import models
from apps.usuarios.models import Usuario

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    icono = models.ImageField(upload_to='iconos/', default='iconos/default_icon.png')

    def __str__(self):
        return self.nombre


class Articulo(models.Model):
    titulo = models.CharField(max_length= 50)
    resumen = models.CharField(max_length = 100, null =True)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to = 'articulos', default='iconos/default_icon.png')
    categoria_articulo = models.ForeignKey(Categoria, on_delete= models.CASCADE)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=Usuario.objects.get(is_superuser=True).pk) 

    def __str__(self):
        return self.titulo