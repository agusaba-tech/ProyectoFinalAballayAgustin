from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm # Formularios de autenticación de usuarios
from django.contrib.auth import login, logout, authenticate  # Funciones para gestionar inicios de sesión y autenticación
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from Users.forms import UserEditForm
from .models  import Avatar
def login_request(request):
    """
    Función para manejar las solicitudes de inicio de sesión.
    """
    if request.method == "POST":  # Si el formulario fue enviado (método POST)
        form = AuthenticationForm(request, data=request.POST)  # Crea un formulario y lo llena con los datos enviados
        print(form)  # Imprime el formulario en la consola (para depuración)

        if form.is_valid():  # Si el formulario es válido
            usuario = form.cleaned_data.get('username')  # Obtiene el nombre de usuario
            clave = form.cleaned_data.get('password')  # Obtiene la contraseña

            nombre_usuario = authenticate(username=usuario, password=clave)  # Intenta autenticar al usuario

            if nombre_usuario is not None:  # Si la autenticación es exitosa
                login(request, nombre_usuario)  # Inicia la sesión del usuario
                return render(request, "Registros/inicio.html", {"mensaje":f"Has iniciado sesión. Bienvenido {usuario}"})  # Renderiza la plantilla con un mensaje de bienvenida
            else:  # Si la autenticación falla
                form = AuthenticationForm()  # Crea un nuevo formulario vacío
                return render(request, "Users/login.html", {"mensaje":"Error, datos incorrectos", "form": form})  # Renderiza el formulario de login con un mensaje de error
        else:  # Si el formulario no es válido
            form = AuthenticationForm()
            return render(request, "Users/login.html", {"mensaje":"Error, datos incorrectos", "form": form})  # Renderiza la plantilla con un mensaje de error

    form = AuthenticationForm()  # Si es una solicitud GET (primera vez que se accede a la página), crea un formulario vacío
    return render(request, "Users/login.html", {"form":form})  # Renderiza el formulario de login

def register(request):

      if request.method == 'POST':

            form = UserCreationForm(request.POST)
            #form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"Registros/inicio.html" ,  {"mensaje":"Usuario Creado :)"})

      else:
            form = UserCreationForm()       
            #form = UserRegisterForm()     

      return render(request,"Users/registro.html" ,  {"form":form})
  
#def Logout(req):
   # return render(req, 'Users/logout.html')

@login_required
def editar_perfil(request):
    
    usuario = request.user  

    if request.method == 'POST': 
        
        miFormulario = UserEditForm(request.POST, request.FILES, instance=usuario) 

        if miFormulario.is_valid():  # Validar los datos del formulario
            if miFormulario.cleaned_data.get('imagen'):
              
                if Avatar.objects.filter(user=usuario).exists():
                    
                    usuario.avatar.imagen= miFormulario.cleaned_data.get('imagen')
                    usuario.avatar.save()
                else:

                    avatar=Avatar(user=usuario, imagen=miFormulario.cleaned_data.get('imagen'))
                    avatar.save()
                
            miFormulario.save()  # Guardar los datos del formulario (incluyendo cualquier otra actualización del perfil)

            return render(request, "Registros/inicio.html")  # Redirigir a la plantilla 'padre.html'

    else:  # Si la solicitud es un GET (carga inicial de la página)
        # Crear una instancia del formulario con los datos del usuario actual pre-llenados
        miFormulario = UserEditForm(instance=usuario) 

    # Renderizar la plantilla 'editar_usuario.html', pasando el formulario y los datos del usuario
    return render(request, "Users/editarUsuario.html", {"miFormulario": miFormulario, "usuario": usuario})

# Create your models here.
class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name='Users/CambiarContrasenia.html'
    success_url=reverse_lazy('EditarPerfil')
    