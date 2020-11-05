from django import forms
from .models import Contacto, Insumo, User
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User

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

class CustomUserCreationForm(UserCreationForm):
    class Meta: 
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]
