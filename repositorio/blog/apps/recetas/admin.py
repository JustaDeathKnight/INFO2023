from django.contrib import admin
from .models import Categoria, Recetas

# Register your models here.
admin.site.register(Recetas)
admin.site.register(Categoria)