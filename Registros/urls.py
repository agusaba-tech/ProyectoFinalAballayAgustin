from django.urls import path
from Registros import views


urlpatterns = [
    path('', views.inicio, name='inicio'),  
    path('Comprador/', views.Comp, name='Comprador'),
    path('Vendedor/', views.Vend, name='Vendedor'),
    path('Producto/', views.Prod, name='Producto'),
    path('busquedaProd/',views.busquedaProd, name= 'Busqueda'),
    path('buscar/',views.buscar)
    
  
    
]