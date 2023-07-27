from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import user_login, user_logout, user_register, user_colab
from . import views

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('registro/', user_register, name='registro'),
    path('colaborador/', user_colab, name='colaborador')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)