from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # роут для отображения страницы
    path('', views.index, name='index'),
    # path('index1', views.index1, name='index1'),
]