from django.shortcuts import render
from .models import Servicio


# Create your views here.
def render_articles(request):
    servicios =Servicio.objects.filter(status=True)
    return render(request, 'articles.html', locals())

