from django.urls import path 
from .views import info_curso,listAlu, crearAlu, actualizarAlu,borrarAlu, profesorLista, profDetalle

urlpatterns=[
    path('info/',info_curso, name= 'info' ),
    path('listAlu/',listAlu, name= 'listAlu' ),
    path('crearAlu/',crearAlu, name= 'crearAlu' ),
    path('borrarAlu/<int:id>/',borrarAlu, name= 'borrarAlu' ),
    path('actualizarAlu/<int:id>/',actualizarAlu, name= 'actualizarAlu' ),
    path('profesores/',profesorLista.as_view(), name= 'profesoresLista' ),
    path('profDetalle/<int:pk>',profDetalle.as_view(), name= 'profDetalle' )
  ] 

