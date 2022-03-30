from django import views
from django.urls import path
from .views import index, plantilla, formulario, busqueda_cursos
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', index, name='index'),
    path('plantilla/', plantilla, name= 'plantilla'),
    path('formulario/', formulario, name= 'formulario'),
    path('busqueda_cursos/', busqueda_cursos, name= 'busqueda_cursos'),
    path('login/', views.login_request, name= 'login'),
    path('registrar/', views.registro, name= 'registro'),
    path('logout/', LogoutView.as_view(template_name = 'index/logout.html'), name= 'logout')
    

]
