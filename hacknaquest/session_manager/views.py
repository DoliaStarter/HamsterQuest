from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'session_manager/index.html', {'page_name': "Session manager"})
