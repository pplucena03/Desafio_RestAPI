from django.db import models

class Event(models.Model):
    titulo = models.TextField(max_length=100, null=False)
    descricao = models.TextField(max_length=200, null=True) #deixar opcional
    data_hora_inicio = models.DateTimeField(null=False)
    data_hora_fim = models.DateTimeField(null=False)