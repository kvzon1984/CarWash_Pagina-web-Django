from django.contrib import admin
from .models import Services, Insumo, Slider, Gallery, Mision , Vision, Contacto

# Register your models here.
#solo se pueden editar casillas que no sean el nombre principal
#list_filter = sirve para agregar filtros en admin

class ServiceAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "price"]
    list_editable = [ "price"]
    search_fields = ["name"] 
    list_per_page = 10

class InsumoAdmin(admin.ModelAdmin):
    list_display = ["name","price","Description", "Stock", "Image"]
    list_editable = [ "price","Stock"]
    search_fields = ["name"]
    list_filter =  ["name","price", "Stock"]
    list_per_page = 10


class SliderAdmin(admin.ModelAdmin):
    list_display = ["name", "image"]
    search_fields = ["name"] 
    list_editable = [ "image"]
    list_filter =  ["name"]
    list_per_page = 10


class GalleryAdmin(admin.ModelAdmin):
    list_display = ["name", "image"]
    search_fields = ["name"]
    list_editable = [ "image"]
    list_filter =  ["name"]
    list_per_page = 10


class MisionAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]
    list_editable = [ "description"]
    search_fields = ["name"] 
    list_per_page = 10

class VisionAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]
    list_editable = [ "description"]
    search_fields = ["name"] 
    list_per_page = 10




admin.site.register(Services, ServiceAdmin)
admin.site.register(Insumo, InsumoAdmin)
admin.site.register(Gallery,GalleryAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(Mision, MisionAdmin)
admin.site.register(Vision, VisionAdmin)
admin.site.register(Contacto)
