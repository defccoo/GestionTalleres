from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


#def index(request):
    
    #return HttpResponse("recursos/Talleres/altaTaller.html")

def homepage(request):
        return render_to_response('homepage.html',
        context_instance=RequestContext(request))