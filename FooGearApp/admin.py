from django.contrib import admin

# Register your models here.
from FooGearApp.models import Stock, Producto, Tienda, Reserva

admin.site.register(Tienda)
admin.site.register(Stock)
admin.site.register(Producto)
admin.site.register(Reserva)