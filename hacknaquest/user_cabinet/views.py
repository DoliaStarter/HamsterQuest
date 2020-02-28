from django.shortcuts import render
from main.models import SomeQuestModel

# Create your views here.

def index(request):
    return render(request, 'user_cabinet/index.html', {'page_name': 'User cabinet'})