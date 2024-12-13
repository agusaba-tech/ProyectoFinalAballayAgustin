from django.urls import path
from Registros import views,views_clases


urlpatterns = [
    path('', views.inicio, name='inicio'),  
    path('Comprador/', views.Comp, name='Comprador'),
    path('Vendedor/', views.Vend, name='Vendedor'),
    path('Producto/', views.Prod, name='Producto'),
    path('busquedaProd/',views.busquedaProd, name= 'Busqueda'),
    path('buscar/',views.buscar),
    path("about/",views.about, name= "about" ),
]

urls_vistas_clases = [
    path('clases/lista/', views_clases.ProductoListView.as_view(), name='List'),
    path('clases/detalle/<int:pk>/', views_clases.ProductoDetalle.as_view(), name='Detail'),
    path('clases/nuevo/', views_clases.ProductoCreateView.as_view(), name='New'),
    path('clases/editar/<int:pk>', views_clases.ProductoUpdateView.as_view(), name='Edit'),
    path('clases/eliminar/<int:pk>', views_clases.ProductoDeleteView.as_view(), name='Delete')
]

urlpatterns+=urls_vistas_clases