from django.shortcuts import render, redirect, get_object_or_404
from .models import Slider, Gallery, Mision, Vision, Insumo
from .forms import ContactoForm, InsumoForm
from django.contrib import messages

# Create your views here.

def index(request):
    slider = Slider.objects.all()
    mision = Mision.objects.all()
    vision = Vision.objects.all()
    data = {
        'slider': slider,
        'mision': mision,
        'vision': vision 
    }
    return render(request, 'app/index.html', data)


def contacto(request):
    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm (data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado" 
        else:
            data["form"] = formulario

    return render(request, 'app/contacto.html',data)

def galeria(request):
    gallery = Gallery.objects.all()
    data = {
        'gallery': gallery
    }

    return render(request, 'app/galeria.html', data)

def registro(request):
    return render(request, 'app/registro.html')

def login(request):
    return render(request, 'app/login.html')


def agregar_insumo(request):

    data = {
        'form' : InsumoForm()
    }
    if request.method == 'POST':
        formulario = InsumoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Agregado correctamente")
        else:
            data["form"] = formulario

    return render(request,'app/insumo/agregar.html',data)

def listar_insumos(request):

    insumos = Insumo.objects.all()
    data = {
        'insumos' : insumos
    }

    return render(request, 'app/insumo/listar.html' , data)


def modificar_insumos(request, id):

    insumo = get_object_or_404(Insumo, id=id)

    data = {
        'form': InsumoForm(instance=insumo)
    }

    if request.method == 'POST':
        formulario = InsumoForm(data=request.POST, instance=insumo, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado correctamente")
            return redirect(to="listar_insumos")

            data["form"] = formulario
             

    return render(request, 'app/insumo/modificar.html',data)

def eliminar_insumos(request, id):
    insumo = get_object_or_404(Insumo, id=id)
    insumo.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="listar_insumos")