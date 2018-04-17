from django.db import models
from django.utils import timezone
import datetime

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Departamento(models.Model):
    idDepart = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=150)


class Alumno(models.Model):
    dni = models.CharField(primary_key=True, max_length=8)
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

#class Profesor(models.Model):

#class ProfesorTaller(models.Model):

