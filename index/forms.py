from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class form_curso(forms.Form):
    curso = forms.CharField(max_length= 100)
    actividad = forms.BooleanField()
    
class buscadorCurso(forms.Form):
    partial_curso = forms.CharField(label = 'Buscar Curso',max_length= 100)

#agregar campos
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label= 'password', widget = forms.PasswordInput)
    password2 = forms.CharField(label= 'password', widget = forms.PasswordInput)
#meta: elemetos que user no ve 

class Meta:
    model = User
    fields = ['username','emails', 'password1', 'password2']
    #Sacar los mensajes de ayuda
    help_texts = {k:"" for k in fields}
   


