from django.http import HttpResponse
from FooGearApp.models import Stock, Producto, Comprador, Reserva

def catalogo(request):
	return HttpResponse("Aquí tienes los tipos de equipaciones %s." % Producto.choice_tipo)

def camisetas(request):
	return HttpResponse("Aquí tienes las camisetas.")

def calzonas(request):
	return HttpResponse("Aquí tienes las calzonas.")

def medias(request):
	return HttpResponse("Aquí tienes las medias.")

def sudaderas(request):
	return HttpResponse("Aquí tienes las sudaderas.")