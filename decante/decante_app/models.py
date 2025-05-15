from django.db import models


class Deudor(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.TextField(blank=True)
    perfumes = models.PositiveIntegerField(default=1)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    abonos = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.nombre

    def restante(self):
        return max(self.balance - self.abonos, 0)



class Pedido(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    direccion = models.TextField()
    empresa = models.CharField(max_length=100)
    pedido = models.TextField()

    def __str__(self):
        return f'{self.nombre} - {self.empresa}'
    
class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    direccion = models.TextField(blank=True)
    empresa = models.CharField(max_length=100, blank=True)
    comentarios = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

