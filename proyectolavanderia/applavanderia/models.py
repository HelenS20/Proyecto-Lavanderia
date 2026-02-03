from django.db import models

class Administrador(models.Model):
    cedulaA = models.CharField(max_length=10, primary_key=True)
    nombreA = models.CharField(max_length=40)
    telefonoA = models.CharField(max_length=10)
    contraseñaA = models.CharField(max_length=15)

class Cliente(models.Model):
    cedulaC = models.CharField(max_length=10, primary_key=True)
    nombreC = models.CharField(max_length=40)
    telefonoC = models.CharField(max_length=10)
    correoC = models.CharField(max_length=50)

class CategoriaPrenda(models.Model):
    idCP = models.CharField(max_length=10, primary_key=True)
    tipoCP = models.CharField(max_length=35)
    descripcionCP = models.CharField(max_length=100)

class TipoServicio(models.Model):
    idTS = models.CharField(max_length=10, primary_key=True)
    nombreTS = models.CharField(max_length=50)
    descripcionTS = models.CharField(max_length=100)
    precio = models.FloatField()

class Prenda(models.Model):
    idP = models.CharField(max_length=10, primary_key=True)
    colorP = models.CharField(max_length=10)
    tipotelaP = models.CharField(max_length=40)
    tipoprendaP = models.CharField(max_length=40)
    idCP = models.ForeignKey(CategoriaPrenda, on_delete=models.CASCADE)

class Facturas(models.Model):
    idF = models.CharField(max_length=10, primary_key=True)
    observacionesF = models.CharField(max_length=100)
    fechayhoraF = models.DateTimeField()
    estadofacturaF = models.CharField(max_length=20)
    cedulaA = models.ForeignKey(Administrador, on_delete=models.CASCADE)
    cedulaC = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class DetalleFactura(models.Model):
    idDF = models.CharField(max_length=10, primary_key=True)
    idF = models.ForeignKey(Facturas, on_delete=models.CASCADE)
    idP = models.ForeignKey(Prenda, on_delete=models.CASCADE)
    idTS = models.ForeignKey(TipoServicio, on_delete=models.CASCADE)

# Create your models here.
