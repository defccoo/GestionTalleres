from django.shortcuts import render,get_object_or_404

# Create your views here.

from django.http import HttpResponse

from .models import Taller, Departamento

def index(request):
    
    return HttpResponse("Hello, world. You're at the polls index.")

def homepage(request):
    return render(request, 'talleres/homepage.html')
        #return render_to_response('homepage.html',
        #context_instance=RequestContext(request))

def acceso(request):
    return render(request, 'talleres/login.html')

def muestraTaller(request):

    taller = get_object_or_404(Taller, pk=1)

    print(taller.descrip)

    return render(request, 'talleres/login.html',
    {
        "taller" : taller
    })

def altataller(request):

    depart_list = Departamento.objects.order_by('-nombre')

    return render(request, 'talleres/altataller.html',
    {
        "depart_list" : depart_list
    })


def creartaller(request):


    print(request.POST.get('descrip', ''))


    """
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

    """

    print("Hello")
    descrip = request.POST.get('descrip', '')
    print("Revisar ESTO!!!")
    idDepart = 1
    departamento = get_object_or_404(Departamento, pk=idDepart)
    nivel = (request.POST.get('nivel', ''))
    curso = int(request.POST.get('curso', ''))
    maxAlum = int(request.POST.get('maxAlum', ''))
    duracion = int(request.POST.get('duracion', ''))
    jornada = int(request.POST.get('jornada', ''))
    excede = int(request.POST.get('excede', ''))


    #El departamento sera el del profesor que ha creado el taller...  
    #
    taller = Taller(descrip=descrip, idDepart=departamento, nivel=nivel, curso=curso, maxAlum=maxAlum, duracion=duracion, jornada=jornada, excede=excede )
    taller.save()
    return listataller(request)
    #...

def listataller(request):

    #Recuperar todos los talleres
    taller_list = Taller.objects.order_by('-curso')[:5]

    print(taller_list)

    return render(request, 'talleres/listaTaller.html',
    {
        "talleres_list" : taller_list,
    })

def muestraTallerConID(request, taller_id):

    taller = get_object_or_404(Taller, pk=taller_id)

    print(taller.descrip)

    return render(request, 'talleres/taller.html',
    {
        "taller" : taller
    })