from django import forms

class FormularioComp (forms.Form):
    Nombre = forms.CharField(max_length=30)
    Apellido = forms.CharField(max_length=30)
class FormularioVend (forms.Form):
    Nombre = forms.CharField(max_length=30)
    Apellido = forms.CharField(max_length=30)
class FormularioProd (forms.Form):
    Nombre = forms.CharField(max_length=30)
    Cantidad = forms.IntegerField()
    
# class Buscar(forms.Form):
#     nombre = forms.CharField(max_length=20)