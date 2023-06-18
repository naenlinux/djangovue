from rest_framework import serializers
from .models import Programador, LenguajeProgra, NuevoPedido

class ProgramadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programador
        #fields = ('nombre','nickname') #solo dos campos seleccionado
        fields = '__all__' #get todos los campos

class LenguajeProgSerializer(serializers.ModelSerializer):
    class Meta:
        model = LenguajeProgra
        fields = '__all__'

class NuevoPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NuevoPedido
        fields = '__all__'