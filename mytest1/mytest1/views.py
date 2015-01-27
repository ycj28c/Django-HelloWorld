from django.http import HttpResponse  
from django.shortcuts import render_to_response  
from django.template import RequestContext, loader  
    #return HttpResponse("Hello, world. You're at the poll index.")    
def index(request):  
    return render_to_response('index.html')  