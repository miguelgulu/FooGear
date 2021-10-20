import uuid
from django.db import models
from django.utils import timezone
# Create your models here.

hoy = timezone.now()

class Tienda(models.Model):
	direccion = models.CharField(max_length=100)
	telefono = models.IntegerField()
	correo = models.EmailField()

	def __str__(self):
		return self.direccion


class Stock(models.Model): 
	tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE, null=True)
	clave_stock = models.CharField(max_length=100, null=True, default="e0001")
	cantidad = models.IntegerField()

	def __str__(self):
		return self.clave_stock


class Producto(models.Model):
	choice_tipo = [('Camiseta', 'Camiseta'), ('Medias', 'Medias'), ('Calzonas','Calzonas'), ('Sudaderas','Sudaderas')]
	choice_talla = [('XS','XS'), ('S','S'), ('M','M'), ('L','L'), ('XL','XL')]
	stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
	tipo = models.CharField(max_length=100, choices=choice_tipo)
	talla = models.CharField(max_length=3, choices=choice_talla)
	precio = models.IntegerField()

	def __str__(self):
		return "Tipo: %s | Talla: %s | Precio: %s" % (self.tipo, self.talla, self.precio)


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
	clave=models.UUIDField(primary_key=True, default=uuid.uuid4)
	fecha=models.DateTimeField('Fecha Reserva', null=True, default=hoy)

	def __str__(self):
		return "%s, %s, %s" % (self.comprador, self.tienda, self.clave)

