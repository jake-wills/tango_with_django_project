from django.urls import path
from rango import views

app_name = 'rango'

urlpatters = [
    path('', views.index, name='index'),
]