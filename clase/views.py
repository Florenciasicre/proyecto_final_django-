# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect, render
from clase.models import Estudiante, Profesor
from clase.form import form_Alu
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


#def company(self):
#    Empresa = empresa(empresa = 'google', cantEmpleados = 40000 )
#    Empresa.save()
#    texto= f"--> Lugar de trabajo: {Empresa.empresa}, compañeros {Empresa.cantEmpleados}"
#    return HttpResponse (texto)



def info_curso(request):
    return render(request, 'clase/info_curso.html',{})


#de#f busqueda_cursos(request):
#  #  cursos_buscados = []
#  # 
#  #  print(request.GET)
#  #  dato = request.GET.get('partial_curso', None#)
#
#  #  if dato is not None:
#  #      cursos_buscados = curso.objects.filter(nombre__icontains = dato#)
#
#  #  buscador_cursos = buscadorCurso()
#  #  return render(request,'index/form_busqueda.html',
#  #  {'buscador_cursos': buscador_cursos ,'cursos_buscados': cursos_buscados})
def listAlu(request):
    listAlu = Estudiante.objects.all()
    return render(request,'clase/listAlu.html',{'listAlu': listAlu })


@login_required
def crearAlu(request):
     if request.method == 'POST':

         form_alu = form_Alu(request.POST)

         if form_alu.is_valid():
          data = form_alu.cleaned_data 
          nuevo_estudiante = Estudiante(nombre = data['nombre'], apellido = data['apellido'], email= data['email'])
          nuevo_estudiante.save()
          return redirect("listAlu")

     form_alu = form_Alu()
     return render(request,'clase/crearAlu.html',{'form_Alu': form_Alu})


def actualizarAlu(request, id):
    estudianteAct = Estudiante.objects.get(id = id)
    
    if request.method == 'POST':
         
         form_alu = form_Alu(request.POST)
         if form_alu.is_valid():
          data = form_alu.cleaned_data 
          estudianteAct.nombre = data['nombre']
          estudianteAct.apellido = data['apellido'] 
          estudianteAct.email= data['email']
          estudianteAct.save()
          return redirect("listAlu")

    form_alu = form_Alu(
        initial={
        'nombre': estudianteAct.nombre,
        'apellido':estudianteAct.apellido,
        'email': estudianteAct.email
        }
    )
    return render(request,'clase/actualizarAlu.html',{'form_Alu': form_Alu, 'estudianteAct': estudianteAct})


def borrarAlu(request, id):
    borrarAlu = Estudiante.objects.get(id = id)
    borrarAlu.delete()
    return redirect('listAlu')


#mixing tiene que estar delante en el ()
class profesorLista(LoginRequiredMixin, ListView):
    model= Profesor
    template_name = './clase/template_prof.html'


class profDetalle(DetailView):
    model= Profesor
    template_name = './clase/profesor_dato.html'


#def crearProf(CreateView):
#   model= Profesor
#   success_url = '/clase/template_prof'
#   field=['nombre', 'apellido', 'profesion']
#
#
#def delete_Prof(DeleteView):
#  model = Profesor
#  success_url= '/clase/template_prof.html'
#
#
#def update_Prof(UpdateView):
#   model = Profesor
#   fields =['nombre', 'apellido', 'profesion']
#   success_url= '/clase/template_prof.html'
#
