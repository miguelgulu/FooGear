from .models import Tienda
from django import forms

choice_tipo = [('Camiseta', 'Camiseta'), ('Medias', 'Medias'), ('Calzonas','Calzonas'), ('Sudaderas','Sudaderas')]
choice_talla = [('XS','XS'), ('S','S'), ('M','M'), ('L','L'), ('XL','XL')]

class ReservaPro(forms.Form):
	tipo = forms.ChoiceField(choices=choice_tipo)
	talla = forms.ChoiceField(choices=choice_talla)
	#tienda = forms.ChoiceField(choices=Tienda.direccion)