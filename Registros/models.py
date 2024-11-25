from django.db import models

# Create your models here.
class Comprador(models.Model):
    Nombre=models.CharField(max_length=30)
    Apellido=models.CharField(max_length=30)
class Vendedor(models.Model):
    Nombre=models.CharField(max_length=30)
    Apellido=models.CharField(max_length=30)
class Producto(models.Model):
    Nombre=models.CharField(max_length=30)
    Cantidad=models.IntegerField()
    
    