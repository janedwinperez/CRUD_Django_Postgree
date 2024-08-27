from django.db import models

# Create your models here.

class Propietarios(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    casa = models.CharField(max_length=10)
    celular = models.CharField(max_length=20)
  
