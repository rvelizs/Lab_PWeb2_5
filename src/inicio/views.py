from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myHomeView(request, *args, **kwards):
    myContext = {
        'myText': 'Esto es sobre nosotros',
        'myNumber': 123,
        'myList': [33, 44,55],
        'myColors': ['red','yellow','pink','purple','blue','two'],
    }
    return render(request,"home.html", myContext)

def anotherView(request):
    return HttpResponse('<h1>Solo otra página</h1>')

# Otra vista
def presentacionView(request):
    return HttpResponse('<h1>Saludos!</h1><br><h2>Soy Rodrigo Véliz Saihua y tengo 18 años</h2>')
