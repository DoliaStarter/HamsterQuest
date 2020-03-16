from django.shortcuts import render


# Create your views here.
from main.models import UserProfile
from main.models import Quests


def index(request):
    return render(request, 'user_cabinet/index.html', {'page_name': 'User cabinet'})


def search_quests(request):
    quests = Quests.objects.order_by('title')
    return render(request, 'user_cabinet/search_quests.html', {'page_name': 'Search Quests', 'quests': quests})
