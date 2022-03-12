
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, loader
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