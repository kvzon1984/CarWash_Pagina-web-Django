from django.shortcuts import render, redirect, get_object_or_404
from .models import Slider, Gallery, Mision, Vision, Insumo
from .forms import ContactoForm, InsumoForm, CustomUserCreationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required

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
            messages.success(request, "Add contact")
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


    data = {
        'form' : CustomUserCreationForm()
    }
    
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)

        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Successful registration")
            return redirect(to="index")
        data["form"] = formulario

    return render(request, 'registration/registro.html', data)



@permission_required('app.add_insumo')    
def agregar_insumo(request):


    data = {
        'form' : InsumoForm()
    }
    if request.method == 'POST':
        formulario = InsumoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Added correctly")
        else:
            data["form"] = formulario

    return render(request,'app/insumo/agregar.html',data)


@permission_required('app.view_insumo') 
def listar_insumos(request):

    insumos = Insumo.objects.all()
    page = request.GET.get('page',1)

    try:
        paginator = Paginator(insumos,10)
        insumos = paginator.page(page)
    except:
        raise Http404


    data = {
        'entity' : insumos,
        'paginator':paginator
    }

    return render(request, 'app/insumo/listar.html' , data)


@permission_required('app.change_insumo') 
def modificar_insumos(request, id):

    insumo = get_object_or_404(Insumo, id=id)

    data = {
        'form': InsumoForm(instance=insumo)
    }

    if request.method == 'POST':
        formulario = InsumoForm(data=request.POST, instance=insumo, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modified Correctly")
            return redirect(to="listar_insumos")

            data["form"] = formulario
             

    return render(request, 'app/insumo/modificar.html',data)


@permission_required('app.delete_insumo') 
def eliminar_insumos(request, id):
    insumo = get_object_or_404(Insumo, id=id)
    insumo.delete()
    messages.success(request, "Deleted correctly")
    return redirect(to="listar_insumos")

