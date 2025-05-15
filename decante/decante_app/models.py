from django.db import models

class Deudor(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.TextField(blank=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    direccion = models.TextField()
    empresa = models.CharField(max_length=100)
    pedido = models.TextField()

    def __str__(self):
        return f'{self.nombre} - {self.empresa}'
