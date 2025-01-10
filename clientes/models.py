from django.db import models
from django.db.models import TextChoices

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    cpf = models.CharField(max_length=12)

    def __str__(self) -> str:
        return self.nome

class Carro(models.Model):
    carro = models.CharField(max_length=50)
    placa = models.CharField(max_length=8)
    ano = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    lavagens = models.IntegerField(default=0)
    consertos = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.carro

class ChoicesCategoriaManutencao(TextChoices):
    TROCAR_VALVULA_MOTOR = "TVM", "Trocar válvula do motor"
    TROCAR_OLEO = "TO", "Troca de óleo"
    BALANCEAMENTO = "BAL", "Balanceamento"

    def __str__(self):
        return self.label

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    categoria_manutencao = models.CharField(
        max_length=3,
        choices=ChoicesCategoriaManutencao.choices,
        default=ChoicesCategoriaManutencao.TROCAR_VALVULA_MOTOR,
    )

    def __str__(self):
        return self.nome