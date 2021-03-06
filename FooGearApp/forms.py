from django import forms
from FooGearApp.models import Reserva, Comprador
from django.contrib.auth.models import User

class ReservaForm(forms.ModelForm):
	class Meta:
		model = Reserva
		exclude = ['clave', 'fecha', 'stock', 'user']

class CompradorCreationForm(forms.ModelForm):
	email = forms.EmailField()
	class Meta:
		model = Comprador
		fields = ('dni', 'telefono', 'direccion', 'email')

