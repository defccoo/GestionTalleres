from django.shortcuts import render,get_object_or_404,redirect

from .forms import TallerForm
# Create your views here.

from django.http import HttpResponse

from .models import Taller, Departamento

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

def homepage(request):
    return render(request, 'talleres/homepage.html')
        #return render_to_response('homepage.html',
        #context_instance=RequestContext(request))

def principal(request):
    return render(request, 'talleres/homepage.html')

def acceso(request):
    return render(request, 'talleres/login.html')

def sitio(request):
    return render(request, 'talleres/local.html')

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

def muestraTallerConID(request, taller_id):

    taller = get_object_or_404(Taller, pk=Numero)

    print(taller.Descripcion)

    return render(request, 'talleres/taller.html',
    {
        "taller" : taller
    })