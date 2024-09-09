from django.db import models

class Categoria(models.Model):
    categoria = models.CharField(max_length=255)
    descricao = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['categoria'] #deixa ordenado 

    def __str__(self):
        return self.categoria  

 