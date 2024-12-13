from django.db import models

# Create your models here.
class Comprador(models.Model):
    Nombre=models.CharField(max_length=30)
    Apellido=models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.Nombre}, {self.Apellido}"

class Vendedor(models.Model):
    Nombre=models.CharField(max_length=30)
    Apellido=models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.Nombre}, {self.Apellido}"
        
        
class Producto(models.Model):
    Nombre=models.CharField(max_length=30)
    Cantidad=models.IntegerField()
    descripcion=models.CharField(max_length=60)
    condicion=models.CharField(max_length=30)
   
   
    def __str__(self):
        return f"{self.Nombre}"   
    