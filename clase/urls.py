from django.urls import path 
from .views import Datos, company, salary, info_curso

urlpatterns=[
    path('Datos/',Datos, name= 'Datos' ),
    path('company/',company, name= 'company' ),
    path('salary/',salary, name= 'salario' ),
    path('info/',info_curso, name= 'info' ),
]