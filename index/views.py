from re import template
from django.http import HttpResponse
from django.template import loader
# Create your views here.


def index(request):
    return HttpResponse('<h1> Bienvenidos</h1>')

def plantilla(request):
    template = loader.get_template('plantilla.html')
    datos = {

    }
    plantilla_generada = template.render (datos)

    return HttpResponse(plantilla_generada)