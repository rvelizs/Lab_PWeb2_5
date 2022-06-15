from django.contrib import admin
from django.urls import path
from inicio.views import myHomeView
from inicio.views import anotherView
from personas.views import personaTestView, personaCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myHomeView, name = 'home'),
    path('another/', anotherView, name = 'otro'),
    path('persona/', personaTestView, name = 'testViewPersona'),
    path('agregar/', presonaCreateView, name = 'createPersona'),
]
