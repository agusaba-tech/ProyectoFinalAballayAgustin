from django.shortcuts import render
from django.http import HttpResponse
from Registros.models import Comprador,Vendedor,Producto
from Registros.forms import FormularioComp,FormularioVend, FormularioProd
from django.contrib.auth.decorators import login_required


def inicio(req):
    return render(req, 'Registros/inicio.html')

def about(req):
    return render(req, 'Registros/about.html')

@login_required
def Comp(request):

    if request.method == "POST": 
        FormC = FormularioComp(request.POST)  
        print(FormC)  
        
        if FormC.is_valid():  
            informacion = FormC.cleaned_data 
            comprador= Comprador(Nombre=informacion["Nombre"], Apellido=informacion["Apellido"]) 
            comprador.save()  
            return render(request, "Registros/inicio.html")  
    else:
        FormC = FormularioComp()  
        
    return render(request, "Registros/Formulario_Comprador.html", {"FormC": FormC})

@login_required
def Vend(request):

    if request.method == "POST": 
        FormV = FormularioVend(request.POST)  
        print(FormV)  
        
        if FormV.is_valid():  
            informacion = FormV.cleaned_data 
            vendedor= Vendedor(Nombre=informacion["Nombre"], Apellido=informacion["Apellido"]) 
            vendedor.save()  
            return render(request, "Registros/inicio.html")  
    else:
        FormV = FormularioVend()  
        
    return render(request, "Registros/Formulario_Vendedor.html", {"FormV": FormV})


def Prod(request):

    if request.method == "POST": 
        FormP = FormularioProd (request.POST)  
        print(FormP)  
        
        if FormP.is_valid():  
            informacion = FormP.cleaned_data 
            producto= Producto(Nombre=informacion["Nombre"], Cantidad=informacion["Cantidad"]) 
            producto.save()  
            return render(request, "Registros/inicio.html")  
    else:
        FormP = FormularioProd()  
        
    return render(request, "Registros/Formulario_Producto.html", {"FormP": FormP})


def busquedaProd(request):
    
    return render(request, "Registros/busquedaProd.html")

def buscar(request):

    if request.GET["prod"]:

          #respuesta = f"Estoy buscando el nro: {request.GET['prod']}"
     
          producto = request.GET['prod']

          cantidad = Producto.objects.filter(Nombre__icontains=producto)

          return render(request, "Registros/resultadosBusqueda.html", {"cantidad": cantidad, "producto": producto})

    else:

          respuesta = "No enviaste datos"

    return HttpResponse(respuesta)