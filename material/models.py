from django.db import models
from categoria.models import Categoria


class Material(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='categorias')
    titulo = models.CharField(max_length=500)    
    patrimonio = models.IntegerField(blank=False, null=False, unique=True)
    descricao = models.TextField(null=True, blank=True)    
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['categoria','titulo']

    def __str__(self):
        return self.titulo    
