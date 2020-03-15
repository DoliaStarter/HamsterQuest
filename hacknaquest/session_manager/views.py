from django.shortcuts import render
from django.http import HttpResponse
from session_manager.forms import SessionManagerMainForm, RadioStages, makeJSON
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json


# Create your views here.

def index(request):
    form = SessionManagerMainForm() 
    radio_stages = RadioStages()
    context = {
        'page_name': "Session manager",
        'form': form,
        'radio_stages': radio_stages,
        'quest_data' : makeJSON()
    }
    return render(request, 'session_manager/index.html', context)


@csrf_exempt
def get_answer(request):
    return HttpResponse(status=200)

@csrf_exempt
def get_data(request) -> dict:
    """Returns data about quest in session."""
    return HttpResponse(status=200)

def save_data(request) -> None:
    """Save user progress"""
    pass
