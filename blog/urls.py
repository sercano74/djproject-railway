from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.render_articles, name='articles'),

]

