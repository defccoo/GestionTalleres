from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    
    return HttpResponse("Hello, world. You're at the polls index.")

def homepage(request):
    return render(request, 'talleres/homepage.html')
        #return render_to_response('homepage.html',
        #context_instance=RequestContext(request))