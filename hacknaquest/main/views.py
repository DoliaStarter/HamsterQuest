from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'main_page/index.html', {'page_name': 'Main page'})
