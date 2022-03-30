from pathlib import Path
from django import views
from django.urls import path
from django.views import View 
from .views import info_curso,listAlu, crearAlu, actualizarAlu,borrarAlu, profesorLista,profDetalle #, update_Prof, crearProf, delete_Prof

urlpatterns=[
    path('info/',info_curso, name= 'info' ),
    path('listAlu/',listAlu, name= 'listAlu' ),
    path('crearAlu/',crearAlu, name= 'crearAlu' ),
    path('borrarAlu/<int:id>/',borrarAlu, name= 'borrarAlu' ),
    path('actualizarAlu/<int:id>/',actualizarAlu, name= 'actualizarAlu' ),


    path('profesores/',profesorLista.as_view(), name= 'profesoresLista' ),
    #path(r'^(?p<pk>\d+)$', profDetalle.as_view(), name= 'Detail' ),
    #path('crearProf', crearProf.as_view(), name= 'crearProf'),
    #path('delete_Prof/<int:id>/', delete_Prof.as_view(), name= 'Delete'),
    #path('update_Prof/<int:id>/', update_Prof.as_view(), name= 'Update'),
  
  ] 


