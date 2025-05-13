from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.render_articles, name='articles'),
    path('articlesxalim/', views.render_articles_alimento, name='articlesxalim'),
    path('articlesxjuego/', views.render_articles_juego, name='articlesxjuego'),
    path('articlesxmob/', views.render_articles_mob, name='articlesxmob'),

]

