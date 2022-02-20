#from django.db import models

from django.db.models import Model,ForeignKey,CASCADE,ImageField
from django.db.models.fields import CharField, IntegerField, EmailField, DateField
from django.contrib.auth.models import User

class Cliente(Model):
    nombre = CharField(max_length=30)
    apellido = CharField(max_length=30)
    email = EmailField()
    telefono = IntegerField()
    
    def __str__(self):
        return f"El cliente es: {self.nombre}, apellido: {self.apellido}, email: {self.email}, telefono: {self.telefono} "
    

class Tragos(Model):
    nombre = CharField(max_length=40)
    precio = IntegerField()
    
    def __str__(self):
        return f'Trago: {self.nombre}, precio: {self.precio} '
    
    
class Evento(Model):
    direccion = CharField(max_length=40)
    altura = IntegerField()
    fecha_evento = DateField()
    
    def __str__(self):
        return f'direccion: {self.direccion}, altura: {self.altura}, fecha del evento: {self.fecha_evento}'
    
class Avatar(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    imagen = ImageField(upload_to='avatares',null=True,blank=True)
    

    

