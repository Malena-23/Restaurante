from django.db import models

# Create your models here.
class MesasEstado(models.Model):
    nombre = models.CharField(max_length=100)    

    def __str__(self):
        return self.nombre
        
class Mesa(models.Model):
        nombre = models.CharField(max_length=200)
        capacidad = models.IntegerField(default=1)
        estado = models.ForeignKey(MesasEstado, on_delete=models.CASCADE, related_name='mesas')

        def __str__(self):
            return self.nombre