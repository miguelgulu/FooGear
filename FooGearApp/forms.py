from django import forms
from FooGearApp.models import Reserva, Comprador
from django.contrib.auth.models import User

# class AnimalForm(forms.Form):
# 	nom = forms.CharField(required=True)
# 	descrip = forms.CharField(required=True)
# 	tipo = forms.CharField(required=True)

class ReservaForm(forms.ModelForm):
	class Meta:
		model = Reserva
		exclude = ['clave', 'fecha', 'stock']

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password', 'email']
