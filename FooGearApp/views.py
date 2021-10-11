from django.http import HttpResponse
from FooGearApp.models import Stock, Producto, Comprador, Reserva, Tienda

def catalogo(request):
	listar_prendas = Producto.objects
	return HttpResponse(listar_prendas)

def camisetas(request):
	return HttpResponse("Aquí tienes las camisetas")

def calzonas(request):
	return HttpResponse("Aquí tienes las calzonas")

def medias(request):
	return HttpResponse("Aquí tienes las medias")

def sudaderas(request):
	return HttpResponse("Aquí tienes las sudaderas")