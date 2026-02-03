from django.urls import  path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('inventario', views.inventario, name='inventario'),
    path('facturacion', views.facturacion, name='facturacion'),
    path('clientes', views.clientes, name='clientes'),
    path('historial', views.historial, name='historial'),
    path('ajustes', views.ajustes, name='ajustes'),

]
