from django.urls import path
from .views import index,contacto, galeria, registro, login

urlpatterns = [
    path('', index, name='index'),
    path('contacto/', contacto, name='contacto'),
    path('galeria/', galeria, name='galeria'),
    path('registro/', registro, name='registro'),
    path('login/', login, name='login')

]