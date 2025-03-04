from django.db import models

class Habito(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data_inicial = models.DateField()
    data_final = models.DateField()

    def __str__(self):
        return self.nome

class Registro(models.Model):
    habito = models.ForeignKey(Habito, on_delete=models.CASCADE)
    data = models.DateField()
    cumprido = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.habito.nome} - {self.data} - {'Cumprido' if self.cumprido else 'Não Cumprido'}"
