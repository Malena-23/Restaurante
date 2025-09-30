from django.db import models

class MesaEstado(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Mesa(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    capacidad = models.IntegerField(null=False)
    estado = models.ForeignKey(MesaEstado, on_delete=models.CASCADE, related_name='mesas_estado')
    
