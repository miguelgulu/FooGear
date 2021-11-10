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
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm, UserCreationForm

from FooGearApp.models import Stock, Producto, Comprador, Reserva, Tienda
from FooGearApp.forms import ReservaForm, UserForm



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

@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class ReservaDetailView(DetailView):

	context_object_name = 'reserva-detail'
	queryset = Reserva.objects.all()

	def get_value_in_qs(queryset, key):
		return queryset.values(key, flat=True)

class ProductoDetailView(DetailView):
	model = Producto


def register(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			#form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password')
			email = form.cleaned_data.get('email')
			nombre = form.cleaned_data.get('nombre')
			telefono = form.cleaned_data.get('telefono')
			direccion = form.cleaned_data.get('direccion')
			user = form.save()
			login(request, user, backend='django.contrib.auth.backends.ModelBackend')
			return redirect('index')
	else:
 		form = UserForm()
	return render(request, 'FooGearApp/register.html', {'form': form})



@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class ReservaCreateView(CreateView):
	model = Reserva
	form_class = ReservaForm
	success_url = reverse_lazy('reserva-view')

@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class ReservaUpdateView(UpdateView):
	model = Reserva
	form_class = ReservaForm
	success_url = reverse_lazy('reserva-view')

@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class ReservaDeleteView(DeleteView):
    model = Reserva
    success_url = reverse_lazy('reserva-view')



def error_404(request, exception):
        data = {}
        return render(request,'FooGearApp/404.html', data)


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

def search_tienda(request):
	if request.method == "POST":
		searched = request.POST['searched']
		tiendas = Tienda.objects.filter(direccion__contains=searched)
		return render(request, 'FooGearApp/search_tienda.html', {'searched': searched, 'tiendas': tiendas})
	else:
		return render(request, 'FooGearApp/search_tienda.html', {})









"""
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Estás logueado como {username}")
                return redirect('/')
            else:
                messages.error(request, "Usuario o contraseña no válidos.")
        else:
            messages.error(request, "Usuario o contraseña no válidos.")
    form = AuthenticationForm()
    return render(request = request, template_name = "FooGearApp/login.html", context={"form":form})


def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			return redirect('FooGearApp/index.html')
	else:
		form = AuthenticationForm()
	return render(request, 'FooGearApp/login.html', {'form':form})
"""
"""
def logout_view(request):
    logout(request)
"""