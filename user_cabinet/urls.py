from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search_quests/', views.search_quests, name='search_quests'),
    path('user_quests/', views.user_quests, name='user_quests'),
    path('quest_description/', views.quest_desription, name='quest_description')
]