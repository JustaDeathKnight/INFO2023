from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Usuario

# Register your models here.
admin.site.register(Usuario)