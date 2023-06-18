#from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ProgramadorSerializer, LenguajeProgSerializer, NuevoPedidoSerializer
from .models import Programador, LenguajeProgra, NuevoPedido

# Create your views here.
class ProgramadorViewSet(viewsets.ModelViewSet):
    queryset = Programador.objects.filter(es_activo = 1)
    serializer_class = ProgramadorSerializer

class LenguajePrograViewSet(viewsets.ModelViewSet):
    queryset = LenguajeProgra.objects.all()
    serializer_class = LenguajeProgSerializer

class NuevoPedidoViewSet(viewsets.ModelViewSet):
    queryset = NuevoPedido.objects.filter(es_activo = 1).order_by('-id')
    serializer_class = NuevoPedidoSerializer
