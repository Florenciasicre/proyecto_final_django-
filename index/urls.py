from django.urls import path
from .views import index, plantilla, formulario, busqueda_cursos
urlpatterns = [
    path('', index, name='index'),
    path('plantilla/', plantilla, name= 'plantilla'),
    path('curso/', formulario, name= 'formulario'),
    path('busqueda_cursos/', busqueda_cursos, name= 'busqueda_cursos')

    

]
