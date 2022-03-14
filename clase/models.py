from django.db import models

class datos(models.Model):
  nombre = models.CharField(max_length= 100)
  profesion = models.CharField( max_length=200)

class empresa(models.Model):
  empresa = models.CharField(max_length=50)
  cantEmpleados = models.IntegerField()

class salario(models.Model):
  salario = models.FloatField()
  aumento = models.FloatField()

    


