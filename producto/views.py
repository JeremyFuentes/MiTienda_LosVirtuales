from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Producto, Contacto
from .forms import ProductoForm, ContactoForm

# Create your views here.
def inicio(request):
    return render(request, 'pages/inicio.html')

def Acerca(request):
    return render(request, 'AcercaDe/AcercaDe.html')

def contacto(request):
    return render(request, 'Contacto/Contacto.html')

def listado_productos(request):
    #Crear variable para almacenar los prodcutos
    productos = Producto.objects.all()
    return render(request, 'producto/productos.html', {'productos': productos})

def crear_producto(request):
    formulario = ProductoForm(request.POST or None)
    if formulario.is_valid():
       # producto = formulario.save
       formulario.save()
       return redirect('productos')
    return render(request, 'producto/crear.html', {'formulario': formulario})

def editar_producto(request, id):
    producto = Producto.objects.get(id = id)
    formulario = ProductoForm(request.POST or None, instance = producto)
    if formulario.is_valid():
        formulario.save()
        return redirect('productos')
    return render(request, 'producto/editar.html', {'formulario': formulario})

def eliminar_producto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect('productos')

def crear_contacto(request):
    Contacto = ContactoForm(request.POST or None)
    if Contacto.is_valid():
       # producto = formulario.save
       Contacto.save()
       return redirect('')
    return render(request, 'producto/crear.html', {'contacto': Contacto})
