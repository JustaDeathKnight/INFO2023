from django.contrib import admin

# Register your models here.
from .models import MensajeContacto

class MensajeAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'mensaje')
    list_filter = ('nombre', 'email')
    search_fields = ('nombre', 'email')

admin.site.register(MensajeContacto, MensajeAdmin)