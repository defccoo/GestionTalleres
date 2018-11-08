from talleres.models import Alumno, Taller, AlumnoTaller, Departamento,Profesor,ProfesorTaller

from django.contrib.auth.models import User

User.objects.create_superuser('quintin', 'quintin@example.com', 'quinto_5')

for i in range(3):
	Departamento.objects.create(idDepart=format(i, '03d'), nombre="depart{:}".format(i, '03d'))

depart=Departamento.objects.all()

for i in range(5):
	Profesor.objects.create(dniP=format(i, '08d'), nombre="projesor{:}".format(i, '03d'), passwd="1234", idDepart=depart[0])

for i in range(100):
	Alumno.objects.create(dniA=format(i, '08d'), nombre="alumno{:}".format(i, '03d'), passwd="1234", curso=1)

##### Crear talleres y lo que falte