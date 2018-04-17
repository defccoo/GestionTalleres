from django.contrib import admin

from .models import Question, Alumno, Taller, AlumnoTaller, Departamento

admin.site.register(Question)
admin.site.register(Alumno)
admin.site.register(Taller)
admin.site.register(AlumnoTaller)
admin.site.register(Departamento)