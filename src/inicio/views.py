from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myHomeView(*args, **kwards):
    return HttpResponse('<h1>Hola Mundo desde Django</h1>')

def anotherView(request):
    return HttpResponse('<h1>Solo otra página</h1>')
