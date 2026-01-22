from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    @property
    def is_gestor(self):
        return hasattr(self, 'gestor')

    @property
    def is_motorista(self):
        return hasattr(self, 'motorista')

class Motorista(models.Model):
    CATEGORIAS = (
        ('A', 'A - Moto'),
        ('B', 'B - Carro'),
        ('AB', 'AB - Moto e Carro'),
        ('C', 'C - Caminhão'),
        ('D', 'D - Ônibus/Van'),
        ('E', 'E - Carreta'),
        ('AC', 'AC - Moto e Caminhão'),
        ('AD', 'AD - Moto e Ônibus'),
        ('AE', 'AE - Moto e Carreta'),
    )

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='motorista')
    cnh = models.CharField(max_length=20, unique=True)
    categoria_cnh = models.CharField(max_length=5, choices=CATEGORIAS, default='B', verbose_name='Categoria da CNH')
    validade_cnh = models.DateField(verbose_name='Validade da CNH')

    def __str__(self):
        return f'{self.user.username} (CNH: {self.categoria_cnh})'

class Gestor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='gestor')
    departamento = models.CharField(max_length=50)
    telefone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.departamento}'