from django.shortcuts import render,redirect
from django.http import HttpResponse
from Appcoder.models import Tragos,Cliente,Evento
from Appcoder.forms import ClienteForm,EventoForm
from django.forms import model_to_dict
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView

def crear_trago(request, precio):
    trago1 = Tragos(nombre= "fernet" ,precio=precio)
    trago1.save()
    
    return HttpResponse(f'Trago creado {precio}$')

def inicio(request):
    return render(request,'Appcoder/inicio.html')
    
def cliente(request):
    return render(request, 'Appcoder/cliente.html',
                  {'cliente': Cliente.objects.all() })
    

    
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
    
def evento(request):
    return render(request, 'Appcoder/evento.html',
                  {'evento': Evento.objects.all() })
    
def evento_add(request):
    if request.method == 'POST':
        formulario = EventoForm(request.POST)
     
        if formulario.is_valid():
            data = formulario.cleaned_data
            Evento.objects.create(
                direccion=data['direccion'],
                altura=data['altura'],
                fecha_evento=data['fecha_evento'])
            return redirect('evento')
    else:
        formulario = EventoForm()    
    return render(request, 'Appcoder/clienteFormulario.html',{'formulario':formulario})

def evento_delete(request,id_evento):
    evento = Evento.objects.get(id=id_evento)
    evento.delete()
    
    return redirect("evento")

def evento_update(request,id_evento):
    if request.method == 'POST':
        formulario = EventoForm(request.POST)
     
        if formulario.is_valid():
            data = formulario.cleaned_data
            
            evento.direccion = data['direccion']
            evento.altura = data['altura']
            evento.fecha_evento = data['fecha_evento']
            
            evento.save()
            
            return redirect('evento')
    else:
        formulario = EventoForm(model_to_dict(evento))    
    return render(request, 'Appcoder/clienteFormulario.html',{'formulario':formulario})

class EventoListView(ListView):
    model = Evento
    template_name = 'Appcoder/evento.html'
    context_object_name = 'evento'
    
class EventoDetailView(DetailView):
    model = Evento
    template_name= 'Appcoder/ver_evento.html'
    
class EventoCreateView(CreateView):
    model = Evento
    success_url =  reverse_lazy('evento')
    fields = ['direccion','altura','fecha_evento']
    template_name = 'Appcoder/evento_form.html'
    
class EventoUpdateView(UpdateView):
    model = Evento
    success_url =  reverse_lazy('evento')
    fields = ['direccion','altura','fecha_evento']
    template_name = 'Appcoder/evento_form.html'
    
class EventoDeleteView(DeleteView):
    model = Evento
    success_url =  reverse_lazy('evento')
    #template_name = 'Appcoder/evento_delete.html'
    