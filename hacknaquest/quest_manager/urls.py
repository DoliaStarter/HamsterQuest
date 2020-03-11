from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_quest', views.create_quest)
]
