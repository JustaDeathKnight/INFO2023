from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return self.nombre

class Recetas(models.Model):
    titulo = models.CharField(max_length=100)
    ingredientes = models.TextField()
    preparacion = models.TextField()
    nota = models.TextField()
    fecha_de_publicacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='recetas')
    categoria_receta = models.ForeignKey(Categoria, on_delete = models.CASCADE)

    def __str__(self) -> str:
        return self.titulo