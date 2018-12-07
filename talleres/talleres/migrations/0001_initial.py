# Generated by Django 2.0.4 on 2018-12-07 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('dniA', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('exp', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=50)),
                ('ape1', models.CharField(max_length=50)),
                ('ape2', models.CharField(max_length=50)),
                ('passwd', models.CharField(max_length=10)),
                ('curso', models.IntegerField()),
                ('nivel', models.CharField(max_length=50)),
                ('grupo', models.CharField(max_length=10)),
                ('activo', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='AlumnoTaller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valora', models.IntegerField(null=True)),
                ('opinion', models.CharField(max_length=150)),
                ('idAlumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='talleres.Alumno')),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('idDepart', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('dniP', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('ape1', models.CharField(max_length=50)),
                ('ape2', models.CharField(max_length=50)),
                ('passwd', models.CharField(max_length=10)),
                ('idDepart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='talleres.Departamento')),
            ],
        ),
        migrations.CreateModel(
            name='ProfesorTaller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('date_start', models.DateTimeField(null=True, verbose_name='Dia Inicio')),
                ('date_end', models.DateTimeField(null=True, verbose_name='Dia Fin')),
                ('hinicio', models.IntegerField(default=0)),
                ('hfin', models.IntegerField(default=0)),
                ('idProfesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='talleres.Profesor')),
            ],
        ),
        migrations.CreateModel(
            name='Taller',
            fields=[
                ('Numero', models.AutoField(primary_key=True, serialize=False)),
                ('NombreTaller', models.CharField(max_length=50)),
                ('Descripcion', models.CharField(max_length=150)),
                ('nivel', models.PositiveSmallIntegerField(choices=[(1, 'ESO'), (2, 'BACHILLER'), (3, 'CFGM'), (4, 'CFGS'), (5, 'PQPI')], null=True)),
                ('curso', models.IntegerField()),
                ('MaxAlumnos', models.IntegerField()),
                ('duracion', models.IntegerField()),
                ('jornada', models.IntegerField()),
                ('excede', models.IntegerField(null=True)),
                ('foto', models.ImageField(blank=True, default='/media/default.jpg', null=True, upload_to='media/')),
                ('estado', models.PositiveSmallIntegerField(choices=[(1, 'abierto'), (2, 'cerrado')], null=True)),
                ('NumDepartamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='talleres.Departamento')),
                ('idAlumnoTaller', models.ManyToManyField(through='talleres.AlumnoTaller', to='talleres.Alumno')),
                ('idProfesorTaller', models.ManyToManyField(through='talleres.ProfesorTaller', to='talleres.Profesor')),
            ],
        ),
        migrations.AddField(
            model_name='profesortaller',
            name='idTaller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='talleres.Taller'),
        ),
        migrations.AddField(
            model_name='alumnotaller',
            name='idTaller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='talleres.Taller'),
        ),
    ]
