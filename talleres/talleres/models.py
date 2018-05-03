from django.db import models
from django.utils import timezone
import datetime
from django.forms.utils import from_current_timezone, to_current_timezone
from django.utils import formats
from django.utils.dateparse import parse_duration
from django.utils.duration import duration_string


class Departamento(models.Model):
    idDepart = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=150)


class Alumno(models.Model):
    dniA = models.CharField(primary_key=True, max_length=8)
    exp = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    ape1 = models.CharField(max_length=50)
    ape2 = models.CharField(max_length=50)
    passwd = models.CharField(max_length=10)
    curso = models.IntegerField()
    nivel = models.CharField(max_length=50)
    grupo = models.CharField(max_length=10)
    activo = models.CharField(max_length=1)
    
class Taller(models.Model):
    idTaller = models.IntegerField(primary_key=True)
    descrip = models.CharField(max_length=150)
    idDepart = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    nivel = models.CharField(max_length=50)
    curso = models.IntegerField()
    maxAlum = models.IntegerField()
    duracion = models.IntegerField()
    jornada = models.IntegerField()
    excede = models.IntegerField()
    idAlumnoTaller = models.ManyToManyField(Alumno, through='AlumnoTaller')

class AlumnoTaller(models.Model):
    idAlumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    idTaller = models.ForeignKey(Taller, on_delete=models.CASCADE)
    

class Profesor(models.Model):
    dniP = models.CharField(primary_key=True, max_length=8)
    nombre = models.CharField(max_length=50)
    ape1 = models.CharField(max_length=50)
    ape2 = models.CharField(max_length=50)
    passwd = models.CharField(max_length=10)
    idDepart = models.ForeignKey(Departamento, on_delete=models.CASCADE)

class ProfesorTaller(models.Model):
    dniP = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    idTaller = models.ForeignKey(Taller, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    date_start = models.DateTimeField('Dia Inicio')
    date_end = models.DateTimeField('Dia Fin')
    hinicio = models.IntegerField(default=0)
    hfin = models.IntegerField(default=0)
  