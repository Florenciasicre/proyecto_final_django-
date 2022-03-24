from django import forms

class form_curso(forms.Form):
    curso = forms.CharField(max_length= 100)
    actividad = forms.BooleanField()
    
class form_busqueda(forms.Form):
    curso = forms.CharField(max_length= 100)

