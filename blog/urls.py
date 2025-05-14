from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.render_articles, name='articles'),
    path('articlesxalim/', views.render_articles_alimento, name='articlesxalim'),
    path('articlesxjuego/', views.render_articles_juego, name='articlesxjuego'),
    path('articlesxmob/', views.render_articles_mob, name='articlesxmob'),

    path('Posteos/', views.Posteos, name='Posteos'),
    path('PostDetail/<int:p_id>', views.PostDetail, name='PostDetail'),
    path('Categoria/<int:c_id>',views.Categoria,name="Categoria"),
    # path('Author/<int:a_id>',views.Author,name="Author"),
    path('Date/<int:month>/<int:year>',views.Date,name="Date"),

]

