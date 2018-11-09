from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import authenticate, login, logout

from .forms import TallerForm
# Create your views here.

from django.http import HttpResponse

from .models import Taller, Departamento, Alumno, AlumnoTaller,Profesor,ProfesorTaller

def getAlumnoByID(dniA):

    alumnos = Alumno.objects.filter(dniA=dniA)

    if len(alumnos) != 0:
        return alumnos[0]
    else:
        return None 

def getAllTalleres():
    return Taller.objects.all()

def getTalleresInscritoByAlumnoID(dniA):
    alumno = getAlumnoByID(dniA)

    if alumno == None:
        return []
    else:
        alumnoTalleres = AlumnoTaller.objects.filter(idAlumno=alumno) 
        talleres = []
        for alumnoTaller in alumnoTalleres:
            #print(dir(alumnoTaller))
            #print(alumnoTaller.idTaller)
            #taller=alumnoTaller.idTaller
            talleres.append(alumnoTaller.idTaller)
            #print(taller)
        return talleres

def getTalleresInscrito(alumno):
    return AlumnoTaller.objects.filter(idAlumno=alumno) 

def getTalleresInscritoByTallerID(alumno, taller_id):

    taller=Taller.objects.filter(Nombre=taller_id)
    return AlumnoTaller.objects.filter(idAlumno=alumno, idTaller=taller) 

def isAlumno(dniA):
    
    alumno=Alumno.objects.filter(dniA=dniA)

    return len(alumno) != 0


def doLogin(request):

    ##Do login
    username = request.POST['dni']
    password = request.POST['pass']
    user = authenticate(username=username, password=password)

    if user is not None:
        # A backend authenticated the credentials

        login(request, user)

        alumno=Alumno.objects.filter(dniA=request.user)

        print(alumno)

        if len(alumno) == 0:
            profesor=Profesor.objects.filter(dniP=request.user)
            return redirect('homepage')
        else:
            return redirect('homepage')

        print("Autenticado")
    else:
        print("No autenticado")
        # No backend authenticated the credentials
    return render(request, 'talleres/homepage.html')

def homepage(request):

    #anonymous user, plain landpage
    if request.user.is_anonymous:
        return render(request, 'talleres/homepage.html')
    else:

        dniA = request.user

        if isAlumno(dniA):

            alumno=getAlumnoByID(dniA)

            talleres=getTalleresInscritoByAlumnoID(dniA)

            return render(request, 'talleres/homepage.html',
                {
                    "alumno" : alumno,
                    "talleres": talleres[:3]
                })

        else:

            return render(request, 'talleres/homepage.html')

        #return render_to_response('homepage.html',
        #context_instance=RequestContext(request))


def taller_new(request):
    if request.method == "POST":
        form = TallerForm(request.POST)
        if form.is_valid():
            taller = form.save(commit=False)
            #post.author = request.user
            taller.save()
            return redirect('/listar')

    else:
        form = TallerForm()
    return render(request, 'talleres/altataller.html', {'form': form})

def index(request):
    
    return HttpResponse("Hello, world. You're at the polls index.")


def logout_view(request):
    logout(request)
    return render(request, 'talleres/homepage.html')

def acceso(request):
    return render(request, 'talleres/login.html')

def sitio(request):
    return render(request, 'talleres/local.html')

def muestraTaller(request):

    taller = get_object_or_404(Taller, pk=1)

    print(taller.Descripcion)

    return render(request, 'talleres/login.html',
    {
        "taller" : taller
    })


def creartaller(request):


    print(request.POST.get('Descripcion', ''))


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
    Descricion = request.POST.get('Descripcion', '')
    print("Revisar ESTO!!!")
    Numero = 1
    departamento = get_object_or_404(Departamento, pk=Numero)
    nivel = (request.POST.get('nivel', ''))
    curso = int(request.POST.get('curso', ''))
    maxAlum = int(request.POST.get('maxAlum', ''))
    duracion = int(request.POST.get('duracion', ''))
    jornada = int(request.POST.get('jornada', ''))
    excede = int(request.POST.get('excede', ''))


    #El departamento sera el del profesor que ha creado el taller...  
    #
    taller = Taller(descrip=Descripcion, idDepart=departamento, nivel=nivel, curso=curso, maxAlum=maxAlum, duracion=duracion, jornada=jornada, excede=excede )
    taller.save()
    return listataller(request)
    #...

def listataller(request):

    #Recuperar todos los talleres
    taller_list = Taller.objects.order_by('-curso')

    print(taller_list)

    return render(request, 'talleres/listaTaller.html',
    {
        "talleres_list" : taller_list,
    })



def listataller(request):

    #Recuperar todos los talleres
    taller_list = Taller.objects.order_by('-curso')

    print(taller_list)

    return render(request, 'talleres/listaTaller.html',
    {
        "talleres_list" : taller_list,
    })


def inscribirse(request):

    taller_id = request.POST["idTaller"]

    taller=Taller.objects.filter(Numero=taller_id)[0]

    alumno=Alumno.objects.filter(dniA=request.user)[0]

    alumnotaller=AlumnoTaller.objects.filter(idAlumno=alumno, idTaller=taller) 

    inscrito = False
    if alumnotaller:
        alumnotaller.delete()
    else:
        alumnotaller=AlumnoTaller.objects.create(idAlumno=alumno, idTaller=taller) 
        inscrito = True

    return render(request, 'talleres/taller.html',
    {
        "taller" : taller,
        "inscrito" : inscrito,
        "alumno" : True
    })


def muestraTallerConID(request, taller_id):

    taller = get_object_or_404(Taller, pk=taller_id)

    alumnos=Alumno.objects.filter(dniA=request.user)

    if request.user.is_anonymous or len(alumnos) == 0:

        return render(request, 'talleres/taller.html',
        {
            "taller" : taller,
            "alumno": False

        })

    else:

        alumno=alumnos[0]

        lista_alumnotaller=AlumnoTaller.objects.filter(idAlumno=alumno, idTaller=taller_id) 

        inscrito = False
        if lista_alumnotaller:
            inscrito = True

        print(lista_alumnotaller)

        print(taller.Descripcion)

        return render(request, 'talleres/taller.html',
        {
            "taller" : taller,
            "inscrito" : inscrito,
            "alumno": True
        })