#from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    #return HttpResponse("Hello there!")
    return render(request, "home.html") #we're applying this template to our view. "request" means we're requesting this template

def about(request):
    #return HttpResponse("My About page")
    return render(request, "about.html")