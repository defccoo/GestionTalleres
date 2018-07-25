from django import forms

from .models import Taller

class TallerForm(forms.ModelForm):

    class Meta:
        model = Taller
        fields = ('nombreT', 'descrip','idDepart','nivel', 'curso','maxAlum','duracion','jornada','excede','foto', 'estado')
"""
idTaller = models.IntegerField(primary_key=True)
nombreT = models.CharField(max_length=50)
descrip = models.CharField(max_length=150)
idDepart = models.ForeignKey(Departamento, on_delete=models.CASCADE)
NIVEL = ((1,'ESO'), (2, 'BACHILLER'), (3,'CFGM'), (4,'CFGS'), (5,'PQPI'))
nivel = models.PositiveSmallIntegerField(choices=NIVEL, null=True)
curso = models.IntegerField()
maxAlum = models.IntegerField()
duracion = models.IntegerField()
jornada = models.IntegerField()
excede = models.IntegerField()
foto = models.ImageField()
ESTADO = ((1, 'abierto'),(2, 'cerrado'))
estado = models.PositiveSmallIntegerField(choices=ESTADO, null=True)
idAlumnoTaller = models.ManyToManyField(Alumno, through='AlumnoTaller')
"""