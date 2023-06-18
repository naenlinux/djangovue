from django.urls import path, include
from rest_framework import routers
from ApiApp import views

router = routers.DefaultRouter()
router.register(r'programadores',views.ProgramadorViewSet)
router.register(r'lenguajes', views.LenguajePrograViewSet)
router.register(r'nuevopedido', views.NuevoPedidoViewSet)

urlpatterns = [
    path('', include(router.urls))
]