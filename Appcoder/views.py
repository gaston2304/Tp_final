from django.shortcuts import render,redirect
from django.http import HttpResponse
from Appcoder.models import Tragos,Cliente
from Appcoder.forms import ClienteForm

def crear_trago(request, precio):
    trago1 = Tragos(nombre= "fernet" ,precio=precio)
    trago1.save()
    
    return HttpResponse(f'Trago creado {precio}$')

def inicio(request):
    return render(request,'Appcoder/inicio.html')
    
def cliente(request):
    return render(request, 'Appcoder/cliente.html',
                  {'cliente': Cliente.objects.all() })
    
def evento(request):
    return render(request, 'Appcoder/evento.html')
    
def tragos(request):
    return render(request, 'Appcoder/tragos.html')

def cliente_formulario(request):
    if request.method == 'POST':
        formulario = ClienteForm(request.POST)
      #  nombre = request.POST['nombre']
      #  apellido = request.POST['apellido']
      #  email = request.POST['email']
      #  telefono = request.POST['telefono']
        if formulario.is_valid():
            data = formulario.cleaned_data
            Cliente.objects.create(nombre=data['nombre'],apellido=data['apellido'],email=data['email'],telefono=data['telefono'])
            return redirect('cliente')
    else:
        formulario = ClienteForm()    
    return render(request, 'Appcoder/clienteFormulario.html',{'formulario':formulario})

def busqueda_clientes(request):
    return render(request, 'Appcoder/busquedaCliente.html')

def buscar(request):
    nombre = request.GET['nombre']
    
    telefono = Cliente.objects.filter(nombre=nombre)
    email = Cliente.objects.filter(nombre=nombre)
    apellido = Cliente.objects.filter(nombre=nombre)
    
    return render(request,'Appcoder/buscar.html',
        {'nombre':nombre,'telefono':telefono,'email':email,'apellido':apellido})
