from django.contrib import admin
from ApiApp.models import Programador, LenguajeProgra, NuevoPedido

# Register your models here.
admin.site.register(
    [
        Programador,
        LenguajeProgra,
        NuevoPedido,
    ]
)