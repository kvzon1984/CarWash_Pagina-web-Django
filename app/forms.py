from django import forms
from .models import Contacto, Insumo
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError



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
    
    def clean_nombre(self):
        name = self.cleaned_data["name"]
        exist = Insumo.objects.filter(name__iexact=name).exists()
        if exist:
            raise ValidationError("Este nombre ya existe")

        return name


    class Meta:
        model = Insumo
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):

    username = forms.CharField(min_length= 3, max_length=80, required=True )
    first_name = forms.CharField(min_length= 3, max_length=80, required=True)
    last_name = forms.CharField(min_length= 3, max_length=80, required=True)
    email =forms.EmailField(required=True)
    


    def clean_email (self):
        email = self.cleaned_data["email"]
        exist = User.objects.filter(email__iexact=email).exists()
        if exist:
            raise ValidationError("Este email ya existe")

        return email


    class Meta: 
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]




