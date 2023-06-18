from django.db import models

# Create your models here.
class Programador(models.Model):
    nombre = models.CharField(max_length=100,blank=True)
    nickname = models.CharField(max_length=50,blank=True)
    edad = models.PositiveSmallIntegerField(blank=True)
    es_activo = models.BooleanField(default=True)

class LenguajeProgra(models.Model):
    nombre = models.CharField(max_length=30)
    anio = models.IntegerField()
    es_activo = models.BooleanField(default=True)

class NuevoPedido(models.Model):
    nombre = models.CharField(max_length=30, blank=True)
    direccion = models.CharField(max_length=40,blank=True)
    hora = models.TimeField(auto_now_add=True,blank=True)
    tiempo = models.TimeField(null=True)
    es_activo = models.BooleanField(default=True)