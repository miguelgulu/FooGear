from django.contrib import admin

# Register your models here.
from FooGearApp.models import Stock, Producto, Tienda, Reserva, Comprador

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class CompradorInline(admin.StackedInline):
    model = Comprador
    can_delete = False
    verbose_name_plural = 'comprador'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (CompradorInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Tienda)
admin.site.register(Stock)
admin.site.register(Producto)
admin.site.register(Reserva)
admin.site.register(Comprador)