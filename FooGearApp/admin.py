from django.contrib import admin

# Register your models here.
from FooGearApp.models import Stock, Producto


admin.site.register(Stock)
admin.site.register(Producto)