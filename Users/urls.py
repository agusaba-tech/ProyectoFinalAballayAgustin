from django.urls import path, include
from Users import views
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('login/',views.login_request, name= "login"),
    path('logout/', LogoutView.as_view(template_name='Users/logout.html'), name='logout'),
    path('registrarse/',views.register , name='registro'),
    path('editarPerfil',views.editar_perfil,name='EditarPerfil'),
    path('CambiarContrasenia',views.CambiarContrasenia.as_view(), name="CambiarContrasenia"),
]