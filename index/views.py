from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, loader
from index.models import curso
from index.forms import buscadorCurso, form_curso, UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout,authenticate

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

      formulario_curso =  form_curso(request.POST) #variable que paso en el template
      
      if formulario_curso.is_valid():

          data = formulario_curso.cleaned_data

          nuevo_curso = curso(nombre = data['curso'], actividad = data['actividad'])

          nuevo_curso.save()

          return render (request,'index/index.html')
  else:
         formulario_curso = form_curso()
  return render(request, 'index/formulario.html',{'formulario_curso': formulario_curso})


        #icontains: nombre (n_varModels) debe contener lo que buscamos. No exactamente igual
        #clase.object, get genera error si no encuentra
def busqueda_cursos(request):
    #request.GET.get: accedo a lo que tiene un elemento del form
    if request.GET["partial_curso"]:
        dato = request.GET["partial_curso"]
        cursos_buscados = curso.objects.filter(nombre__icontains = dato)
        return render(request,'index/form_busqueda.html',{'cursos_buscados': cursos_buscados})
    else:
        respuesta = 'No enviaste datos'
    return HttpResponse(respuesta)


#con usuario desde pane
def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username = username, password = password)
            if user is not None:
                login(request,user)
                return render(request,"index/index.html", {'mensaje': 'Bienvenido, te logiaste!!'})
            else:
                return render(request,"index/login.html", {'form': form,'mensaje': 'Error, falta informacion'})
        else:
            return render(request,"index/login.html", {'form': form, 'mensaje': 'Error, formulario erroneo'})
    form = AuthenticationForm()
    return render (request, 'index/login.html',{'form': form})

#sin usuario desde panel 
def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) # Si formulario de django uso UserCreationForm
        
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return request(request, 'index/index.html',{'mensaje': f'Usuario creado {username}'})

    else:
           form = UserRegisterForm()
           return render(request, 'index/registro.html',{'form': form, 'mensaje': ''})

    return render(request, 'index/registro.html',{'form': form})

