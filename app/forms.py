from django import forms
from .models import Contacto, Insumo
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError
from django.core.validators import validate_slug

from .Validators import MaxsizeFileValidator, MaxLengthValidator


#fields = ["name1", "name2"] deben ser los mismos campos de models

class ContactoForm(forms.ModelForm):

    name = forms.CharField(min_length=3, max_length=50)
    last_name = forms.CharField(min_length=3 ,max_length=50)
    subject = forms.CharField(min_length=8 ,max_length=50)
    message = forms.CharField( min_length=10, max_length=200 ,widget=forms.Textarea())


    def clean_name(self):
        name = self.cleaned_data["name"]
        if not name.isalpha():
            raise forms.ValidationError("The name cannot contain numbers")
        return name



    class Meta:
        model = Contacto
        fields = '__all__' 
# trae todos los campos de models contacto


class InsumoForm(forms.ModelForm):

    name = forms.CharField(min_length= 3, max_length=120, required=True)
    price = forms.IntegerField(min_value=1, required=True)
    Image = forms.ImageField(required=False, validators=[MaxsizeFileValidator(max_file_size=2)])
    Description = forms.CharField( min_length=3, max_length=120, required=True ,widget=forms.Textarea())
    Stock = forms.IntegerField(min_value=0, required=True)
    
    def clean_nombre(self):
        name = self.cleaned_data["name"]
        exist = Insumo.objects.filter(name__iexact=name).exists()
        if exist:
            raise ValidationError("This name already exists. Please try again ")

        return name


    class Meta:
        model = Insumo
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):

    username = forms.CharField(min_length= 3, max_length=80, required=True )
    first_name = forms.CharField(min_length= 3, max_length=80, required=True)
    last_name = forms.CharField(min_length= 3, max_length=80, required=True)
    email =forms.EmailField(required=True)
    
    def clean_first_name(self):
        first_name = self.cleaned_data["first_name"]
        if not first_name.isalpha():
            raise forms.ValidationError("The name cannot contain numbers")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data["last_name"]
        if not last_name.isalpha():
            raise forms.ValidationError("The name cannot contain numbers")
        return last_name




    def clean_email (self):
        email = self.cleaned_data["email"]
        exist = User.objects.filter(email__iexact=email).exists()
        if exist:
            raise ValidationError("This email already exists. Please try again")

        return email


    class Meta: 
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]




