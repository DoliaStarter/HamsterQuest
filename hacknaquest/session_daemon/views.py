from django.shortcuts import render
from django.http import HttpResponse
from main.models import SomeQuestModel

# Create your views here.

def index(request):
    return HttpResponse("You are in session manager app")