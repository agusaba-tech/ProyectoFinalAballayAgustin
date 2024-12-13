from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User


class UserEditForm(UserChangeForm):
    password=None
    email= forms.EmailField(label="Ingrese email:")
    last_name=forms.CharField(label='Apellido')
    first_name=forms.CharField(label='Nombre')
    imagen=forms.ImageField(label="Avatar",required=False)
    
    
    class Meta:
        model= User
        fields=['email','last_name','first_name', 'imagen']
    