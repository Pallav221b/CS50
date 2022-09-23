from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def pallav(request):
    return HttpResponse("Hello, pallav!")

def dubey(request):
    return HttpResponse("Hello, dubey!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name" : name.capitalize()
    })