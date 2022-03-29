from django.db import models

class Estudiante(models.Model):
  nombre = models.CharField(max_length=50)
  apellido = models.CharField(max_length=200)
  email= models.EmailField()
  def __str__(self):
      return f"{self.nombre} {self.apellido}"


class Profesor(models.Model):
  nombre = models.CharField(max_length=50)
  apellido = models.CharField(max_length=200)
  profesion= models.CharField(max_length=50)
  def __str__(self):
      return f"{self.nombre} {self.apellido}"
  


    


