from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)    

    def __str__(self):
        return self.nombre
    
class Platillo(models.Model):
        nombre = models.CharField(max_length=200)
        descripcion = models.TextField()
        precio = models.DecimalField(max_digits=10, decimal_places=2)
        categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='platillos')

        def __str__(self):
            return self.nombre
        
class Mesa(models.Model):
    ESTADO_CHOICES = [
        ('disponible', 'Disponible'),
        ('ocupada', 'Ocupada'),
    ]
    
    nombre = models.CharField(max_length=100)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='disponible')
    
    def __str__(self):
        return self.nombre