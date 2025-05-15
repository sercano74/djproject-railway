from .models import *
from datetime import date
from django.core.paginator import Paginator
from django.shortcuts import render,redirect,get_object_or_404 as go404


# Create your views here.
#*###########################################################################################
#*                                 MODELO DE ARTICULOS
#*###########################################################################################
def render_articles(request):
    articulos = Articulo.objects.filter(status=True)
    return render(request, 'articles.html', locals())

def render_articles_alimento(request):
    articulos = Articulo.objects.filter(status=True, type='alimento')
    return render(request, 'articles.html', locals())

def render_articles_juego(request):
    articulos = Articulo.objects.filter(status=True, type='juego')
    return render(request, 'articles.html', locals())

def render_articles_mob(request):
    articulos = Articulo.objects.filter(status=True, type='mobiliario')
    return render(request, 'articles.html', locals())


#*###########################################################################################
#*                                  MODELO DE BLOGS
#*###########################################################################################
def Posteos(request):
    if request.method == 'GET':
        if not request.session.get('items_per_page'):
            request.session['items_per_page'] = 2
        if 'items_per_page' in request.GET:
            request.session['items_per_page'] = int(request.GET['items_per_page'])

        items_per_page = request.session['items_per_page']

        last = Post.objects.filter(published=True).last()
        first = Post.objects.filter(published=True).first()
        publis_page = Paginator(Post.objects.filter(published=True),items_per_page)
        page = request.GET.get('page')
        publis = publis_page.get_page(page)
        aux =  'X' * publis.paginator.num_pages
        return render (request,'Posteos.html',locals())

def PostDetail(request,p_id):
    if request.method=='GET':
        try:
            publi = go404(Post,id=p_id)
            print('publi ===============>>>  ',publi)
            page_number = request.GET.get('page')
            return render(request, 'PostDetail.html', {'publi': publi, 'previous_page': page_number})
        except:
            message = "Posteo seleccionado, no existe o está inactivo !!"
            return render(request, '404.html', {'previous_page': request.GET.get('page')})

def Categoria(request,c_id):
    if request.method=='GET':
        try:
            categoria = go404(CtgPost,pk=c_id)
            return render (request,'Categoria.html',locals())
        except:
            message="Categoría seleccionada, no existe o está inactiva !!"
            return render(request, '404.html', locals())

#* Quedará pendiente hasta que se implemente la app de usuarios y permisos
# def Author(request, a_id):
#     if request.method=='GET':
#         try:
#             author = go404(User,pk=a_id)
#             # publi = go404(Post,author=author)
#             return render (request,'Ap01Blog/Author.html',locals())
#         except:
#             message="Autor seleccionado, no existe o está inactivo !!"
#             return render(request, '404.html', locals())

# @register.simple_tag
def get_mes(n):
    meses = {
        1:'Enero',
        2:'Febrero',
        3:'Marzo',
        4:'Abril',
        5:'Mayo',
        6:'Junio',
        7:'julio',
        8:'Agosto',
        9:'Septiembre',
        10:'Octubre',
        11:'Noviembre',
        12:'Diciembre',
    }
    mess = meses[n]
    # print('mess ================>>>  ',mess)
    return meses.get(n," Mes inválido")

def Date(request,month,year):
    messi = get_mes(month)
    fecha = date(year,month,1).isoformat() # YYYY-MM-DD
    posts = Post.objects.filter(published=True, created__month=month, created__year=year)
    return render (request,'Date.html', locals())

