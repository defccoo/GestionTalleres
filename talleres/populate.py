from talleres.models import Alumno, Taller, AlumnoTaller, Departamento,Profesor,ProfesorTaller

from django.contrib.auth.models import User

User.objects.create_superuser('quintin', 'quintin@example.com', 'quinto_5')

for i in range(3):
	Departamento.objects.create(idDepart=format(i, '03d'), nombre="depart{:}".format(i, '03d'))

depart=Departamento.objects.all()

for i in range(5):
	Profesor.objects.create(dniP=format(i, '04d'), nombre="projesor{:}".format(i, '03d'), passwd="1234", idDepart=depart[0])

for i in range(100):
	Alumno.objects.create(dniA=format(i, '08d'), nombre="alumno{:}".format(i, '03d'), passwd="1234", curso=1)


profesores=Profesor.objects.all()

for profesor in profesores:
	user = User.objects.create_user(profesor.dniP, '{:}@ejemplo.com'.format(profesor.nombre), '1234')

alumnos=Alumno.objects.all()

for alumno in alumnos:
	user = User.objects.create_user(alumno.dniA, '{:}@ejemplo.com'.format(alumno.nombre), '1234')

##### Crear talleres y lo que falte

for i in range(10):
	Taller.objects.create(Numero=format(i, '04d'), NombreTaller="Taller{:}".format(i, '03d'), curso=1, MaxAlumnos=10, Descripcion="Taller ...{:}".format(i, '03d'), duracion=5, jornada=1, NumDepartamento=depart[0])

talleres=Taller.objects.all()


for i in range(10):
	if i < 5:
		AlumnoTaller.objects.create(idAlumno=alumnos[i], idTaller=talleres[0])
	else:
		AlumnoTaller.objects.create(idAlumno=alumnos[i], idTaller=talleres[1])
