from django.db import models

# Create your models here.

class Stock(models.Model): 
	idstock = models.IntegerField()

class Producto(models.Model):
	choice_tipo = [('C', 'Camiseta'), ('M', 'Medias'), ('CL','Calzonas'), ('S','Sudaderas')]
	choice_talla = [('XS','XS'), ('S','S'), ('M','M'), ('L','L'), ('XL','XL')]
	idstock = models.ForeignKey(Stock, on_delete=models.CASCADE)
	tipo = models.CharField(max_length=100, choices=choice_tipo) #Choice
	talla = models.CharField(max_length=3, choices=choice_talla) #Choice
	cantidad = models.IntegerField()
	precio = models.IntegerField()

class Comprador(models.Model):
	nombre=models.CharField(max_length=100)
	telefono=models.IntegerField()
	direccion=models.CharField(max_length=150)

class Reserva(models.Model):
	producto=models.ManyToManyField(Producto)
	comprador=models.ForeignKey(Comprador, on_delete=models.CASCADE)
	idReserva=models.IntegerField()