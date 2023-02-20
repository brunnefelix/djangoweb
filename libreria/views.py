from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hola mundo prueba 1</h1>")

def nosotros(request):
    return HttpResponse("<h1>Prueba 2</h1>")

def contacto(request):
    return HttpResponse("<h1>Prueba 3</h1>")

def paginaUno(request):
    return HttpResponse("<h1>Prueba 4</h1>")
                        
def paginaDos(request):
    return HttpResponse("<h1>Prueba 5</h1>")

def paginaTres(request):
    return HttpResponse("<h1>Prueba 6</h1")

def paginaCuatro(request):
    return HttpResponse("<h1>Prueba 7</h1")

def paginaCinco(request):
    return  HttpResponse("<h1>Prueba 8</h1")

def paginaSeis(request):
    return  HttpResponse("<h1>Prueba 9</h1")

def paginaSiete(request):
    return HttpResponse("<h1>Prueba 10</h1")

def paginaOcho(request):
    return HttpResponse("<h1>Prueba 11</h1")

def paginaNueve(request):
    return HttpResponse("<h1>Prueba 12</h1")

def paginaDiez(request):
    return HttpResponse("<h1>Prueba 13</h1")

def paginaOnce(request):
    return  HttpResponse("<h1>Prueba 14</h1")


# Create your views here.