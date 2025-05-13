from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_home, name='home'),
    path('contacto/', views.contacto, name='contacto'),

]

