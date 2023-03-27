from django.db import models

class Juguete(models.Model):
    nombre = models.CharField(max_length=30)
    tamaño = models.CharField(max_length=30)
    color = models.CharField(max_length=15)
    marca = models.CharField(max_length=10)
    cantidad = models.CharField(max_length=3)
    
