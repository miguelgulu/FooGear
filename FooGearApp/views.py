from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from FooGearApp.models import Stock, Producto, Comprador, Reserva, Tienda
from django.template import loader
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from FooGearApp.forms import ReservaForm, CompradorForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


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

def index(request):
	template = loader.get_template('FooGearApp/index.html')
	return HttpResponse(template.render())


class ReservaDetailView(DetailView):

	context_object_name = 'reserva-detail'
	queryset = Reserva.objects.all()

	def get_value_in_qs(queryset, key):
		return queryset.values(key, flat=True)

class ProductoDetailView(DetailView):
	queryset = Producto.objects.all()

	def get_object(self):
		obj = super().get_object()
		obj.save()
		return obj

class CompradorCreateView(CreateView):
	model = Comprador
	form_class = CompradorForm
	success_url = reverse_lazy('comprador-view')



class ReservaCreateView(CreateView):
	model = Reserva

	form_class = ReservaForm
	success_url = reverse_lazy('reserva-view')

class ReservaUpdateView(UpdateView):
	model = Reserva
	form_class = ReservaForm
	success_url = reverse_lazy('reserva-view')

class ReservaDeleteView(DeleteView):
    model = Reserva
    success_url = reverse_lazy('reserva-view')


def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			return redirect('FooGearApp/reserva_list.html')
	else:
		form = AuthenticationForm()
	return render(request, 'FooGearApp/login.html', {'form':form})

def logout_view(request):
    logout(request)
