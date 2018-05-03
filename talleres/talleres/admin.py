from django.contrib import admin

from .models import  Alumno, Taller, AlumnoTaller, Departamento,Profesor,ProfesorTaller

admin.site.register(Alumno)
admin.site.register(Taller)
admin.site.register(AlumnoTaller)
admin.site.register(Departamento)
admin.site.register(Profesor)
admin.site.register(ProfesorTaller)