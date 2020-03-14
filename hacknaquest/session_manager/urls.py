from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_answer', views.get_answer),
    path('get_data', views.get_data)
]