from django import forms
from FooGearApp.models import Reserva, Comprador
from django.contrib.auth.models import User

class ReservaForm(forms.ModelForm):

	class Meta:
		model = Reserva
		exclude = ['clave', 'fecha', 'stock', 'comprador']

class UserForm(forms.ModelForm):
	email = forms.EmailField(widget=forms.EmailInput, help_text='Obligatorio')
	password = forms.CharField(max_length=254, widget=forms.PasswordInput)
	
	nombre = forms.CharField(required = True)
	telefono = forms.IntegerField(required = True)
	direccion = forms.CharField(required = True)

	class Meta:
		model = User
		fields = ('username', 'email', 'password', 'nombre', 'telefono', 'direccion')
"""
	def save(self, commit=True):
		user = super(UserForm, self).save(commit=False)
		if commit:
			user.save()
		return user
"""