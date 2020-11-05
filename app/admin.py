from django.contrib import admin
from .models import Services, Insumo, Slider, Gallery, Mision , Vision, Contacto, User
from .forms import InsumoForm

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
    form = InsumoForm


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


class ContactoAdmin(admin.ModelAdmin):
    list_display = ["query_type","name", "email", "message","notices"]
    list_editable = [ "name", "email"]
    search_fields = ["query_type","name"] 
    list_filter =  ["query_type"]
    list_per_page = 10

class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "last_name",  "email"]
    list_editable = [ "last_name",  "email"]
    search_fields = ["username", ] 
    list_per_page = 10




admin.site.register(Services, ServiceAdmin)
admin.site.register(Insumo, InsumoAdmin)
admin.site.register(Gallery,GalleryAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(Mision, MisionAdmin)
admin.site.register(Vision, VisionAdmin)
admin.site.register(Contacto,ContactoAdmin)
admin.site.register(User, UserAdmin)
