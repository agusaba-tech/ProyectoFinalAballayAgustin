from .models import Producto  # Importa el modelo "Curso" desde tu aplicación
from django.views.generic import ListView  # Para mostrar listas de objetos
from django.views.generic.detail import DetailView  # Para mostrar detalles de un objeto
from django.views.generic.edit import CreateView, UpdateView, DeleteView  # Para crear, actualizar y eliminar objetos
from django.urls import reverse_lazy  # Para generar URLs de forma segura

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm  # Formularios de autenticación de usuarios
from django.contrib.auth import login, logout, authenticate  # Funciones para gestionar inicios de sesión y autenticación

class ProductoListView(ListView):
    """
    Vista para mostrar una lista de todos los cursos.
    """
    model = Producto  # Modelo con el que trabaja esta vista
    template_name = "registros/Vistas_Clases/producto_list.html"  # Plantilla para renderizar la lista

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
    success_url = reverse_lazy("List")  # URL de redirección después de crear un curso
    fields = ["Nombre", "Cantidad","descripcion","condicion"]  # Campos del modelo a mostrar en el formulario

class ProductoUpdateView(UpdateView):
    """
    Vista para editar cursos existentes a través de un formulario
    """
    model = Producto
    template_name = "registros/Vistas_Clases/producto_edit.html"
    success_url = reverse_lazy("List")
    #success_url = "/clases/lista/"  # Otra forma de especificar la URL de redirección
    fields = ["Nombre", "Cantidad","descripcion","condicion"]

class ProductoDeleteView(DeleteView):
    """
    Vista para eliminar cursos.
    """
    model = Producto
    success_url = reverse_lazy("List")  # URL de redirección después de eliminar un curso
    template_name = "registros/Vistas_Clases/producto_confirm_delete.html"  # Plantilla para confirmar la eliminación