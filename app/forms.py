from django import forms
from .models import Contacto, Insumo, User
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User




from .Validators import MaxsizeFileValidator, MaxLengthValidator


#fields = ["name1", "name2"] deben ser los mismos campos de models

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__' 
# trae todos los campos de models contacto


class InsumoForm(forms.ModelForm):

    name = forms.CharField(min_length= 3, max_length=120, required=True)
    price = forms.IntegerField(min_value=1, required=True)
    Image = forms.ImageField(required=False, validators=[MaxsizeFileValidator(max_file_size=2)])
    Description = forms.CharField(min_length=3, max_length=120, required=False)
    Stock = forms.IntegerField(min_value=0, required=True)
    

    class Meta:
        model = Insumo
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    class Meta: 
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]
