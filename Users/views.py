from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm 
from django.contrib.auth import login, logout, authenticate  
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
    if request.method == "POST":  
        form = AuthenticationForm(request, data=request.POST)  
        print(form)  

        if form.is_valid(): 
            usuario = form.cleaned_data.get('username')  
            clave = form.cleaned_data.get('password')  
            
            nombre_usuario = authenticate(username=usuario, password=clave)  

            if nombre_usuario is not None:  
                login(request, nombre_usuario)  
                return render(request, "Registros/inicio.html", {"mensaje":f"Has iniciado sesión. Bienvenido {usuario}"})  
            else:  
                form = AuthenticationForm()  
                return render(request, "Users/login.html", {"mensaje":"Error, datos incorrectos", "form": form}) 
        else:  
            form = AuthenticationForm()
            return render(request, "Users/login.html", {"mensaje":"Error, datos incorrectos", "form": form})  

    form = AuthenticationForm()  
    return render(request, "Users/login.html", {"form":form})  

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
  


@login_required
def editar_perfil(request):
    
    usuario = request.user  

    if request.method == 'POST': 
        
        miFormulario = UserEditForm(request.POST, request.FILES, instance=usuario) 

        if miFormulario.is_valid(): 
            if miFormulario.cleaned_data.get('imagen'):
              
                if Avatar.objects.filter(user=usuario).exists():
                    
                    usuario.avatar.imagen= miFormulario.cleaned_data.get('imagen')
                    usuario.avatar.save()
                else:

                    avatar=Avatar(user=usuario, imagen=miFormulario.cleaned_data.get('imagen'))
                    avatar.save()
                
            miFormulario.save()  

            return render(request, "Registros/inicio.html")  

    else:  
        miFormulario = UserEditForm(instance=usuario) 

    
    return render(request, "Users/editarUsuario.html", {"miFormulario": miFormulario, "usuario": usuario})

# Create your models here.
class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name='Users/CambiarContrasenia.html'
    success_url=reverse_lazy('EditarPerfil')
    