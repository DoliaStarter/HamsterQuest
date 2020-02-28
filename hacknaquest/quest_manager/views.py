from django.shortcuts import render
from main.models import SomeQuestModel

# Create your views here.

def index(request):
    return render(request, 'quest_manager/index.html', {'page_name': 'Quest manager'})
