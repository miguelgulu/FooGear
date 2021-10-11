from django.db import models
from django.utils import timezone
# Create your models here.

hoy = timezone.now()

class Tienda(models.Model):
	direccion = models.CharField(max_length=100)
	telefono = models.IntegerField()
	correo = models.EmailField()


#Añadir modelo y stock. Stock es la interrelacion de tienda y producto

class Stock(models.Model): 
	tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE, null=True)
	cantidad = models.IntegerField()

	def __int__(self):
		return self.cantidad


class Producto(models.Model):
	choice_tipo = [('Camiseta', 'Camiseta'), ('Medias', 'Medias'), ('Calzonas','Calzonas'), ('Sudaderas','Sudaderas')]
	choice_talla = [('XS','XS'), ('S','S'), ('M','M'), ('L','L'), ('XL','XL')]
	stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
	tipo = models.CharField(max_length=100, choices=choice_tipo)
	talla = models.CharField(max_length=3, choices=choice_talla)
	precio = models.IntegerField()

	def __str__(self):
		return self.tipo, self.talla, self.precio	


class Comprador(models.Model):
	nombre=models.CharField(max_length=100)
	telefono=models.IntegerField()
	direccion=models.CharField(max_length=150)

	def __str__(self):
		return self.nombre

class Reserva(models.Model):
	producto=models.ManyToManyField(Producto)
	comprador=models.ForeignKey(Comprador, on_delete=models.CASCADE)
	tienda=models.ForeignKey(Tienda, on_delete=models.CASCADE, null=True)
	fecha=models.DateTimeField('Fecha Reserva', null=True, default=hoy)


	def __repr__(self):
		return "%s %s %s" % (self.producto, self.comprador, self.tienda)

