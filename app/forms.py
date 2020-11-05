from django import forms
from .models import Contacto, Insumo

#fields = ["name1", "name2"] deben ser los mismos campos de models

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__' 
# trae todos los campos de models contacto


class InsumoForm(forms.ModelForm):
    class Meta:
        model = Insumo
        fields = '__all__'