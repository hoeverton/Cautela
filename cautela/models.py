from django.db import models
from policial.models import Policial
from material.models import Material


class Cautela(models.Model):
    STATUS_CHOICES = [
        ('aberto', 'Em aberto'),
        ('fechado', 'Fechado'),
    ]
    status = models.CharField(max_length=7, choices=STATUS_CHOICES, default='aberto')
    data = models.DateTimeField(auto_now_add=True)
    furriel = models.ForeignKey(Policial, on_delete=models.PROTECT, related_name='cautela_furriel')
    material = models.ForeignKey(Material, on_delete=models.PROTECT, related_name='materiais')
    opcao = models.CharField(max_length=200, null=True, blank=True)
    solicitante = models.ForeignKey(Policial, on_delete=models.PROTECT, related_name='cautela_solicitante')
    data_entrega = models.DateTimeField(auto_now_add=True)
    entregador  = models.ForeignKey(Policial, on_delete=models.PROTECT, related_name='cautela_entregador',null=True, blank=True)
    recebedor = models.ForeignKey(Policial, on_delete=models.PROTECT, related_name='cautela_recebedor', null=True, blank=True)
    alteracao = models.TextField(null=True, blank=True)

    def __str__(self):
        return {self.id}, {self.data}, {self.furriel}, {self.material},{self.opcao}, {self.entregador}, {self.recebedor}, {self.alteracao}, {self.status}
     
