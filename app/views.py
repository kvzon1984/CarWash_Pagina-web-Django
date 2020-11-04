from django.shortcuts import render
from .models import Slider ,Gallery

# Create your views here.

def index(request):
    slider = Slider.objects.all()
    data = {
        'slider': slider
    }
    return render(request, 'app/index.html')

def contacto(request):
    return render(request, 'app/contacto.html')

def galeria(request):
    gallery = Gallery.objects.all()
    data = {
        'gallery': gallery
    }

    return render(request, 'app/galeria.html')

def registro(request):
    return render(request, 'app/registro.html')

def login(request):
    return render(request, 'app/login.html')

