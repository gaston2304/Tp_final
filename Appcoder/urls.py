from django.urls import path
from Appcoder.views import EventoDetailView, EventoDeleteView, EventoCreateView, EventoListView,evento_update,evento_delete,evento_add,crear_trago, inicio,cliente,tragos,evento,cliente_formulario,buscar,busqueda_clientes,EventoUpdateView

urlpatterns = [
    path('creartrago/<precio>', crear_trago),
    path('', inicio, name='inicio'),
    path('cliente', cliente, name='cliente'),
    path('tragos', tragos, name = 'tragos'),
    path('evento', evento, name = 'evento'),
    path('clienteFormulario', cliente_formulario, name = 'cliente_formulario'),
    path('busquedaClientes', busqueda_clientes, name = 'busqueda_clientes'),
    path('buscar', buscar, name = 'buscar'),
    #path('evento', evento, name = 'evento'),
    #path('evento/add', evento_add, name = 'evento_add'),
    #path('evento/delete/<id_evento>', evento_delete, name = 'evento_delete'),
    #path('evento/update/<id_evento>', evento_update, name = 'evento_update'),
    path('evento', EventoListView.as_view(), name = 'evento'),
    path('evento/add', EventoCreateView.as_view(), name = 'evento_add'),
    path('evento/update/<pk>', EventoUpdateView.as_view(), name = 'evento_update'),
    path('evento/delete/<pk>', EventoDeleteView.as_view(), name = 'evento_delete'),
    path('evento/view/<pk>', EventoDetailView.as_view(), name = 'evento_view'),
]