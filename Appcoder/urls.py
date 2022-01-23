from django.urls import path
from Appcoder.views import crear_trago, inicio,cliente,tragos,evento,cliente_formulario,buscar,busqueda_clientes

urlpatterns = [
    path('creartrago/<precio>', crear_trago),
    path('', inicio, name='inicio'),
    path('cliente', cliente, name='cliente'),
    path('tragos', tragos, name = 'tragos'),
    path('evento', evento, name = 'evento'),
    path('clienteFormulario', cliente_formulario, name = 'cliente_formulario'),
    path('busquedaClientes', busqueda_clientes, name = 'busqueda_clientes'),
    path('buscar', buscar, name = 'buscar'),
    
]