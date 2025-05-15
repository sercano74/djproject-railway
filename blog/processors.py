from .models import*




# Inyección de diccionarios

# ABOUT
def ctx_dic_about(request):
    ctx_about={}
    ctx_about['ABOUT']=About.objects.latest('created')
    # print('-----------------------------------------------')
    # print('About -----> ',ctx_about['ABOUT'])
    # About ----->  Desarrolamos ingenierías
    print('-----------------------------------------------')
    return ctx_about

# Categorias
def ctx_dic_cat(request):
    ctx_cat={}
    ctx_cat['CAT']=CtgPost.objects.filter(active=True)
    # print('-----------------------------------------------')
    # print('ctx_cat -----> ',ctx_cat)
    # # About ----->  Desarrolamos ingenierías
    # print('-----------------------------------------------')
    return ctx_cat

# dates

# Redes Sociales
def ctx_dic_link(request):
    ctx_link={}
    links=Link.objects.all()
    for link in links:
        # print('LINK -----> ',link)
        # SE FORMA UN NUEVO DICCIONARIO CON CLAVE(link.key) Y UN VALOR QUE TB ES UN DICT
        ctx_link[link.key]={'url':link.url,'icon':link.icon}
    # print('-----------------------------------------------')
    # print(ctx_link)
    # print('-----------------------------------------------')
    # for value in ctx_link.values():
        # print('value["url"] ---->  ', value['url'])
    # print('-----------------------------------------------')
    # for key in ctx_link.keys():
    #     print('key - value["url"] -->',key,' - ',ctx_link[key]['url'])
    # print('-----------------------------------------------')
    # for key,value in ctx_link.items():
    #     print('value -->',key,' - ',value)
    return ctx_link

# Archivos por periodo
def ctx_dic_history(request):
    ctx_history = {}
#Creamos un dict que consulta hasta el mes pasando por el año
    ctx_history['dates'] = Post.objects.dates('created','month',order='DESC').distinct()
    # print('ctx_history ================>> ',ctx_history)
#ctx_history ================>>  {'dates': <QuerySet [datetime.date(2024, 8, 1), datetime.date(2024, 7, 1), datetime.date(2024, 5, 1), datetime.date(2024, 3, 1), datetime.date(2023, 8, 1), datetime.date(2023, 7, 1)]>}
    return ctx_history


