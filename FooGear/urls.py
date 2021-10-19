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
from FooGearApp.views import Form_reserva, StockListView, ReservaDetailView, ReservaListView, CompradorListView, ProductoListView, TiendaListView, ProductoDetailView 

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.catalogo, name='index'),
    path('tiendas/', TiendaListView.as_view()),
    path('stock/', StockListView.as_view()),
    path('productos/', ProductoListView.as_view()),
    path('compradores/', CompradorListView.as_view()),
    path('reservas/', ReservaListView.as_view()),
    path('reservas/<str:pk>', ReservaDetailView.as_view(), name='reserva-detail'),
    path('productos/<int:pk>/', ProductoDetailView.as_view(), name='product-detail'),
    path('', Form_reserva),
]
