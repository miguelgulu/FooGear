from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from FooGearApp.models import Stock, Producto, Comprador, Reserva, Tienda

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
	context_object_name= 'Reserva'


class StockProductoListView(ListView):
	template_name = "FooGearApp/productos_de_stock.html"

	def get_queryset(self):
		self.stock = get_list_or_404(Producto, stock=self.kwargs['clave_stock'])
		return Producto.objects.filter(stock=self.stock)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['Stock'] = self.stock
		return context

class ProductoDetailView(DetailView):
	queryset = Producto.objects.all()

	def get_object(self):
		obj = super().get_object()
		obj.save()
		return obj