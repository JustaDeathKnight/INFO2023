from django.urls import path
from .views import user_login, user_logout, user_register, user_colab
from . import views

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('registro/', user_register, name='registro'),
    path('colab/', user_colab, name='colab')
]