from django.urls import path
from .views import index, plantilla, formulario, Buscador
urlpatterns = [
    path('', index, name='index'),
    path('plantilla/', plantilla, name= 'plantilla'),
    path('curso/', formulario, name= 'formulario'),
    path('Buscador/', Buscador, name= 'Buscador')

    

]
