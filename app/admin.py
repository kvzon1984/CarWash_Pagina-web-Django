from django.contrib import admin
from .models import Services, Insumo, Slider, Gallery

# Register your models here.
#solo se pueden editar casillas que no sean el nombre principal
class ServiceAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "price"]
    list_editable = [ "price"]
    search_fields = ["name"]
    #list_filter = sirve para agregar filtros en admin 
    list_per_page = 5

admin.site.register(Services, ServiceAdmin)
admin.site.register(Insumo)
admin.site.register(Gallery)
admin.site.register(Slider)