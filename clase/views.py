

# Create your views here.
from django.http import HttpResponse
from clase.models import datos,empresa,salario
def Datos(self):
    Datos = datos(nombre = 'Flor', profesion = 'est')
    Datos.save()
    texto = f"--> Nombre {Datos.nombre} profesion {Datos.profesion} "
    return HttpResponse(texto)
def company(self):
    Empresa = empresa(empresa = 'google', cantEmpleados = 40000 )
    Empresa.save()
    texto= f"--> Lugar de trabajo: {Empresa.empresa}, compañeros {Empresa.cantEmpleados}"
    return HttpResponse (texto)
def salary(self):
    Salario = salario(salario = '90000', aumento = '0' )
    Salario.save()
    textoSalario = f"--> Salario {Salario.salario}, aumento {Salario.aumento}"
    return HttpResponse (textoSalario)