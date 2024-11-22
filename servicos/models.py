from django.db import models
from clientes.models import Cliente


class CategoriaManutencao(models.Model):
    titulo = models.CharField(max_length=3)
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    def _str_(self) -> str:
        return self.titulo
    
class Servico(models.Model):
    titulo = models.CharField(max_length=30)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)

    data_inicio = models.DateField(null=True)
    data_entrega = models.DateField(null=True)
    finalizado = models.BooleanField(default=False)
    protocole = models.CharField(max_length=32, null=True, blank=True)

    #aula 5, 08:38 minuto 
