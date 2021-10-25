"""FooGear URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from FooGearApp.views import index, StockListView,  ReservaListView, CompradorListView, ProductoListView, TiendaListView
from FooGearApp.views import ReservaDetailView, ProductoDetailView 
from FooGearApp.views import ReservaCreateView, ReservaUpdateView, ReservaDeleteView, CompradorCreateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('tiendas/', TiendaListView.as_view(), name='tiendas-view'),
    path('stock/', StockListView.as_view(), name='stock-view'),
    path('productos/', ProductoListView.as_view(), name='producto-view'),
    path('compradores/', CompradorListView.as_view(), name='comprador-view'),
    path('reservas/', ReservaListView.as_view(), name='reserva-view'),
    path('reservas/<str:pk>', ReservaDetailView.as_view(), name='reserva-detail'),
    path('productos/<int:pk>/', ProductoDetailView.as_view(), name='product-detail'),
    path('compradores/add/', CompradorCreateView.as_view(), name='comprador-add'),
    path('reservas/add/', ReservaCreateView.as_view(), name='reserva-add'),
    path('reservas/<str:pk>/update', ReservaUpdateView.as_view(), name='reserva-update'),
    path('reservas/<str:pk>/delete/', ReservaDeleteView.as_view(), name='reserva-delete'),
    path('FooGearApp/login/', auth_views.LoginView.as_view(), name='login'),
]
