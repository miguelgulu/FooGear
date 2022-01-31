from django.shortcuts import get_object_or_404, get_list_or_404, render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.template import loader
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm, UserCreationForm

from FooGearApp.models import Stock, Producto, Comprador, Reserva, Tienda
from FooGearApp.forms import ReservaForm, CompradorCreationForm

import operator

# -------------- Vistas genéricas -----------------

class TiendaListView(ListView):
	model = Tienda
	context_object_name= 'Tiendas'
	permission_required = ('Tienda.view_choice', 'Tienda.change_choice')

class StockListView(ListView):
	model = Stock
	context_object_name= 'Stocks Disponibles'

class ProductoListView(ListView):
	model = Producto
	context_object_name= 'Productos'

@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class CompradorListView(ListView):
	model = Comprador
	context_object_name= 'Compradores'

@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class ReservaListView(ListView):
	model = Reserva

def index(request):
	return render(request, 'FooGearApp/index.html')

# -------------- Vistas detalle -----------------

@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class ReservaDetailView(DetailView):

	context_object_name = 'reserva-detail'
	queryset = Reserva.objects.all()

	def get_value_in_qs(queryset, key):
		return queryset.values(key, flat=True)

class ProductoDetailView(DetailView):
	model = Producto

# -------------- Formularios de registro -----------------

def register(request):
	if request.method == 'POST':
		uform = UserCreationForm(request.POST)
		cform = CompradorCreationForm(request.POST)
		if uform.is_valid() and cform.is_valid():
			user = uform.save(commit=False)
			comprador = cform.save(commit=False)
			comprador.user = user
			email = cform.cleaned_data.get('email')
			user.email = email
			uform.save()
			cform.save()
			return redirect('index')
	else:
		uform = UserCreationForm()
		cform = CompradorCreationForm()
	return render(request, 'FooGearApp/register.html', {'uform': uform, 'cform': cform})

# -------------- Vistas de actualización -----------------


@login_required
def reserva(request):
	if request.method == 'POST':
		form = ReservaForm(request.POST)
		if form.is_valid():
			reserva = form.save(commit=False)
			reserva.user = request.user
			#compra = reserva.producto
			form.save()
			messages.success(request, '¡Reserva realizada con éxito!')
			return redirect('index')
	else:
		form = ReservaForm()
	return render(request, 'FooGearApp/reserva_form.html', {'form': form})



@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class ReservaUpdateView(UpdateView):
	model = Reserva
	form_class = ReservaForm
	success_url = reverse_lazy('reserva-view')



@user_passes_test(operator.attrgetter('is_staff'))
class ReservaDeleteView(DeleteView):
    model = Reserva
    success_url = reverse_lazy('reserva-view')

# -------------- Vista error -----------------

def error_404(request, exception):
        data = {}
        return render(request,'FooGearApp/404.html', data)


# -------------- Cambio de contraseña -----------------

def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)
			user.save()
			messages.success(request, 'Tu contraseña ha sido actualizada!')
			return redirect('index')
		else:
			messages.error(request, 'Por favor, comprueba bien los campos.')
	else:
		form = PasswordChangeForm(request.user)
	return render(request, 'FooGearApp/change_password.html', {'form': form})

# -------------- Buscador de tiendas -----------------

def search_producto(request):
	if request.method == "POST":
		searched = request.POST['searched']
		productos = Producto.objects.filter(tipo__contains=searched)
		return render(request, 'FooGearApp/search_producto.html', {'searched': searched, 'productos': productos})
	else:
		return render(request, 'FooGearApp/search_producto.html', {})

def products_index(request):

    producto_gen = Producto.objects.order_by('?')[:4]

    context = {
        'producto_gen': producto_gen,
    }

    return render(request, 'FooGearApp/index.html', context)