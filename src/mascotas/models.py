from django.db import models

# Create your models here.
class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=300)
    dueño = models.CharField(max_length=50)
    tiempo = models.IntegerField()