from django.urls import path
from .views import index, contacto, galeria, registro, agregar_insumo, listar_insumos, modificar_insumos, eliminar_insumos

urlpatterns = [
    path('', index, name="index"),
    path('contacto/', contacto, name="contacto"),
    path('galeria/', galeria, name="galeria"),
    path('registro/', registro, name="registro"),
    path('agregar-insumo/', agregar_insumo,name="agregar_insumo"),
    path('listar-insumos/', listar_insumos,name="listar_insumos"),
    path('modificar-insumos/<id>/', modificar_insumos, name="modificar_insumos"),
    path('eliminar-insumos/<id>/', eliminar_insumos, name="eliminar_insumos"),

]