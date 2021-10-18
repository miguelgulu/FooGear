from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from FooGearApp.models import Stock, Producto, Comprador, Reserva, Tienda
from .forms import ReservaPro

class TiendaListView(ListView):
	model = Tienda
	context_object_name= 'Tiendas'

class StockListView(ListView):
	model = Stock
	context_object_name= 'Stocks Disponibles'

class ProductoListView(ListView):
	model = Producto
	context_object_name= 'Productos'

class CompradorListView(ListView):
	model = Comprador
	context_object_name= 'Compradores'

class ReservaListView(ListView):
	model = Reserva


class ProductoReservaListView(ListView):

	template_name = 'FooGearApp/productos_reserva.html'

	def get_queryset(self):
		self.reserva = get_object_or_404(Reserva, clave=self.kwargs['reserva'])
		return Producto.objects.filter(publisher=self.reserva)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['reserva'] = self.reserva
		return context



class ProductoDetailView(DetailView):
	queryset = Producto.objects.all()

	def get_object(self):
		obj = super().get_object()
		obj.save()
		return obj

def Form_reserva(request):
    context = {}
    context['form'] = ReservaPro()
    return render( request, "templates/FooGearApp/encargo.html", context)