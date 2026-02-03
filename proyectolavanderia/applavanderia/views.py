from django.shortcuts import render
def index (request):
        return render (request, 'paginas/index.html')

def inventario (request):
        return render (request, 'paginas/inventario.html')

def facturacion (request):
        return render (request, 'paginas/facturacion.html')

def clientes (request):
        return render (request, 'paginas/clientes.html')

def historial (request):
        return render (request, 'paginas/historial.html')

def ajustes (request):
        return render (request, 'paginas/ajustes.html')