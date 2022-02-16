from django.forms import Form, CharField, IntegerField, EmailField,DateField

class ClienteForm(Form):
    nombre = CharField()
    apellido = CharField()
    email = EmailField()
    telefono = IntegerField()
    
class EventoForm(Form):
    direccion = CharField(max_length=30)
    altura = IntegerField()
    fecha_evento = DateField()