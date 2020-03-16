from django.urls import path

from . import views

urlpatterns = [
    path('user_cabinet/', views.index, name='index'),
    path('search_quests/', views.search_quests, name='search_quests')
]