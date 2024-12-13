from .models import Producto  
from django.views.generic import ListView  
from django.views.generic.detail import DetailView  
from django.views.generic.edit import CreateView, UpdateView, DeleteView  
from django.urls import reverse_lazy  

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm 
from django.contrib.auth import login, logout, authenticate  

class ProductoListView(ListView):
    """
    Vista para mostrar una lista de todos los cursos.
    """
    model = Producto  
    template_name = "registros/Vistas_Clases/producto_list.html"  

class ProductoDetalle(DetailView):
    """
    Vista para mostrar los detalles de un curso específico.
    """
    model = Producto
    template_name = "registros/Vistas_Clases/producto_detalle.html"

class ProductoCreateView(CreateView):
    """
    Vista para crear nuevos cursos a través de un formulario.
    """
    model = Producto
    template_name = "registros/Vistas_Clases/producto_form.html"
    success_url = reverse_lazy("List")  
    fields = ["Nombre", "Cantidad","descripcion","condicion"]  

class ProductoUpdateView(UpdateView):
    """
    Vista para editar cursos existentes a través de un formulario
    """
    model = Producto
    template_name = "registros/Vistas_Clases/producto_edit.html"
    success_url = reverse_lazy("List")
    
    fields = ["Nombre", "Cantidad","descripcion","condicion"]

class ProductoDeleteView(DeleteView):
    """
    Vista para eliminar cursos.
    """
    model = Producto
    success_url = reverse_lazy("List")  
    template_name = "registros/Vistas_Clases/producto_confirm_delete.html" 