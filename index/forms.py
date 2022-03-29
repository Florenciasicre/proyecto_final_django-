from django import forms

class form_curso(forms.Form):
    curso = forms.CharField(max_length= 100)
    actividad = forms.BooleanField()
    
class buscadorCurso(forms.Form):
    partial_curso = forms.CharField(label = 'Buscar Curso',max_length= 100)

