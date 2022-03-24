from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, loader
from index.models import curso
from index.forms import buscadorCurso, form_curso

# Create your views here.

def index(request):
    return render(request, 'index/index.html',{})

def plantilla(request):
    dato = {
    'nombre': 'primer',
    'edad': '40'
   }
    #template = loader.get_template('mi_plantilla.html')

   # plantilla_generada = template.render({})
    #return HttpResponse(plantilla_generada)
    return render(request, 'index/mi_plantilla.html', dato)

def Curso(self):
    Curso = curso(nombre = 'a', actividad = 0 )
    Curso.save()
    texto = f" CURSO {Curso.nombre},actividad {Curso.actividad}"
    return HttpResponse (texto)

#Formulario sin django   
#def formulario_curso(request):
#    if request.method == 'POST':
#        Curso_nuevo = curso(nombre = reques.POST['curso'], actividad = reques.POST['actividad'] )
#        Curso_nuevo.save()
#        return render(request, 'index/formulario.html',{'curso_nuevo' : Curso_nuevo}) 
#    return render(request, 'index/formulario.html',{}) 
# --> con form html :  Curso: <input type= 'text' name = 'curso'></input>
                       # Estado: <input type= 'boolean' name= 'actividad'></input>
#formulario con django 

def formulario(request):
  if request.method == 'POST':
      formulario_curso =  form_curso(request.POST)
      if formulario_curso.is_valid():
          data = formulario_curso.cleaned_data 
          nuevo_curso = curso(nombre = data['curso'], actividad = data['actividad'] )
          nuevo_curso.save()
          return render (request,'index/index.html')
  else:
         formulario_curso = form_curso()
  return render(request, 'index/formulario.html',{'formulario_curso': formulario_curso})


        #icontains: nombre (n_varModels) debe contener lo que buscamos. No exactamente igual
        #clase.object, get genera error si no encuentra
def busqueda_cursos(request):
    cursos_buscados = []
    #request.GET.get: accedo a lo que tiene un elemento del form
    print(request.GET)
    dato = request.GET.get('partial_curso', None)

    if dato is not None:
        cursos_buscados = curso.objects.filter(nombre__icontains = dato)

    buscador_cursos = buscadorCurso()
    return render(request,'index/form_busqueda.html',
    {'buscador_cursos': buscador_cursos ,'cursos_buscados': cursos_buscados})



    