from django.db import models
from django.utils import timezone
import datetime
from django.forms.utils import from_current_timezone, to_current_timezone
from django.utils import formats
from django.utils.dateparse import parse_duration
from django.utils.duration import duration_string
from django.urls import reverse


class Departamento(models.Model):
    idDepart = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre


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

    def __str__(self):
        return self.nombre
    

"""class Taller(models.Model):
    idTaller = models.AutoField(primary_key=True)
    nombreT = models.CharField(max_length=50)
    descrip = models.CharField(max_length=150)
    idDepart = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    NIVEL = ((1,'ESO'), (2, 'BACHILLER'), (3,'CFGM'), (4,'CFGS'), (5,'PQPI'))
    nivel = models.PositiveSmallIntegerField(choices=NIVEL, null=True)
    curso = models.IntegerField()
    maxAlum = models.IntegerField()
    duracion = models.IntegerField()
    jornada = models.IntegerField()
    excede = models.IntegerField(null=True)
    foto = models.ImageField(blank=True, null=True)
    ESTADO = ((1, 'abierto'),(2, 'cerrado'))
    estado = models.PositiveSmallIntegerField(choices=ESTADO, null=True)
    idAlumnoTaller = models.ManyToManyField(Alumno, through='AlumnoTaller')
"""
class Taller(models.Model):
    Numero = models.AutoField(primary_key=True)
    NombreTaller = models.CharField(max_length=50)
    Descripcion = models.CharField(max_length=150)
    NumDepartamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    NIVEL = ((1,'ESO'), (2, 'BACHILLER'), (3,'CFGM'), (4,'CFGS'), (5,'PQPI'))
    nivel = models.PositiveSmallIntegerField(choices=NIVEL, null=True)
    curso = models.IntegerField()
    MaxAlumnos = models.IntegerField()
    duracion = models.IntegerField()
    jornada = models.IntegerField()
    excede = models.IntegerField(null=True)
    foto = models.ImageField(blank=True, null=True, upload_to = 'media/', default='/media/default.jpg')
    ESTADO = ((1, 'abierto'),(2, 'cerrado'))
    estado = models.PositiveSmallIntegerField(choices=ESTADO, null=True)
    idAlumnoTaller = models.ManyToManyField(Alumno, through='AlumnoTaller')

    def get_absolute_url(self):
        return reverse('taller_update', kwargs={'pk': self.Numero})


    def __str__(self):
        return self.NombreTaller

class AlumnoTaller(models.Model):
    idAlumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    idTaller = models.ForeignKey(Taller, on_delete=models.CASCADE)
    valora = models.IntegerField(null=True)
    opinion = models.CharField(max_length=150)


class Profesor(models.Model):
    dniP = models.CharField(primary_key=True, max_length=8)
    nombre = models.CharField(max_length=50)
    ape1 = models.CharField(max_length=50)
    ape2 = models.CharField(max_length=50)
    passwd = models.CharField(max_length=10)
    idDepart = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
   
    

class ProfesorTaller(models.Model):
    dniP = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    idTaller = models.ForeignKey(Taller, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    date_start = models.DateTimeField('Dia Inicio')
    date_end = models.DateTimeField('Dia Fin')
    hinicio = models.IntegerField(default=0)
    hfin = models.IntegerField(default=0)
  
