from django.shortcuts import render
from .models import Servicio


# Create your views here.
def render_articles(request):
    servicios =Servicio.objects.filter(status=True)
    return render(request, 'articles.html', locals())

def render_articles_alimento(request):
    servicios =Servicio.objects.filter(status=True, type='alimento')
    return render(request, 'articles.html', locals())

def render_articles_juego(request):
    servicios =Servicio.objects.filter(status=True, type='juego')
    return render(request, 'articles.html', locals())

def render_articles_mob(request):
    servicios =Servicio.objects.filter(status=True, type='mobiliario')
    return render(request, 'articles.html', locals())