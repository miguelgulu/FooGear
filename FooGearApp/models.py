import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

hoy = timezone.now()

class Tienda(models.Model):
	direccion = models.CharField(max_length=100)
	telefono = models.IntegerField()
	correo = models.EmailField()

	def __str__(self):
		return self.direccion


class Producto(models.Model):
	tipo = models.CharField(max_length=100)
	marca = models.CharField(max_length=100)
	precio = models.IntegerField()
	imagen = models.ImageField(upload_to='productos')

	def __str__(self):
		return self.tipo

class Stock(models.Model): 
	tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE, null=True)
	producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
	clave_stock = models.CharField(max_length=100, null=True, default="e0001")
	cantidad = models.IntegerField()

	def __str__(self):
		return self.clave_stock


class Comprador(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	dni=models.CharField(max_length=10)
	telefono=models.IntegerField()
	direccion=models.CharField(max_length=150)

	def __str__(self):
		return self.dni

class Reserva(models.Model):
	producto=models.ManyToManyField(Producto)
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	tienda=models.ForeignKey(Tienda, on_delete=models.CASCADE, null=True)
	clave=models.UUIDField(primary_key=True, default=uuid.uuid4)
	fecha=models.DateTimeField('Fecha Reserva', null=True, default=hoy)

	def __str__(self):
		return "%s, %s, %s" % (self.user.username, self.tienda, self.clave)

