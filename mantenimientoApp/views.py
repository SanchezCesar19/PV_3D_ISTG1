from django.shortcuts import render
from mantenimientoApp.models import eliminacion_ventas
# Create your views here.
def elicompra(request):
    return render(request,'eliminacion_compra.html',{})

def eliventa(request):
    return render(request,'eliminacion_venta.html',{})

from .models import eliminacion_compras

def obtener_eliminacionescompra():
    # Obtener todos los objetos de eliminacion_compras
    eliminacionescompra = eliminacion_compras.objects.all()
    # Modificar el estado de cada objeto
    for eliminacion in eliminacionescompra:
        eliminacion.estado = 1  # o 0 si prefieres
        eliminacion.save()
    # Retornar los objetos modificados
    return eliminacionescompra

def obtener_eliminacionesventas():
    eliminacionesven = eliminacion_ventas.objects.all()
    for eliminacion in eliminacionesven:
        eliminacion.estado = 1
        eliminacion.save()
    return eliminacionesven