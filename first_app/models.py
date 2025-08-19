from django.db import models

class Investimento(models.Model):
    tipo_investimento = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()

    def __str__(self):
        return self.tipo_investimento
