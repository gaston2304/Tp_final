from django.forms import Form, CharField, IntegerField, EmailField

class ClienteForm(Form):
    nombre = CharField()
    apellido = CharField()
    email = EmailField()
    telefono = IntegerField()