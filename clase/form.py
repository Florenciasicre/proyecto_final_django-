from django import forms

class form_Alu(forms.Form):
    nombre = forms.CharField(max_length= 50)
    apellido = forms.CharField(max_length=200)
    email= forms.EmailField()

