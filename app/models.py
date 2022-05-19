from django.db import models

# Create your models here.

class Usuario(models.Model):
    """ Cadastro de Usuarios """
    nome = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True, unique=True)
    senha = models.CharField(max_length=100, blank=True, null=True)