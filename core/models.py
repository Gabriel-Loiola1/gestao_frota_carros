from django.db import models
from contas.models import Motorista

class Veiculo(models.Model):
    STATUS = (
        ('disponivel', 'Disponível'),
        ('em_uso', 'Em Uso'),
        ('manuntencao', 'Manuntenção')
    )

    modelo = models.CharField(max_length=50)
    placa = models.CharField(max_length=7, unique=True)
    km_atual = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS, default='disponivel')

    def __str__(self):
        return f'{self.modelo} - {self.placa}'

class Movimentacao(models.Model):
    motorista = models.ForeignKey(Motorista, on_delete=models.PROTECT)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.PROTECT)
    data_saida = models.DateTimeField(auto_now_add=True)
    km_saida = models.PositiveIntegerField()
    data_retorno = models.DateTimeField(null=True, blank=True)
    km_retorno = models.PositiveIntegerField(null=True, blank=True)
    observacao = models.TextField(blank=True)