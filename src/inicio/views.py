from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myHomeView(request, *args, **kwards):
    print(args, kwards)
    print(request.user)
    return render(request,"home.html", {})

def anotherView(request):
    return HttpResponse('<h1>Solo otra página</h1>')

# Otra vista
def presentacionView(request):
    return HttpResponse('<h1>Saludos!</h1><br><h2>Soy Rodrigo Véliz Saihua y tengo 18 años</h2>')
