from django.db import models
from django.contrib.auth.models import User

class Juguete(models.Model):
    nombre = models.CharField(max_length=30)
    tamaño = models.CharField(max_length=30)
    color = models.CharField(max_length=15)
    marca = models.CharField(max_length=10)
    cantidad = models.CharField(max_length=3)
    publisher = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="publisher")
    image = models.ImageField(upload_to="juguetes", null=True, blank=True)
    #creado_el = models.DateTimeField(auto_now_add=True)

    @property
    def image_url(self):
        return self.image.url if self.image else ''

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(upload_to="avatares", null=True, blank=True)

class Mensaje(models.Model):
    mensaje = models.TextField(max_length=1000)
    email = models.EmailField()
    creado_el = models.DateTimeField(auto_now_add=True) 
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mensajes")