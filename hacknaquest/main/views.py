from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    # later it will be a request to database.
    user_count = 1_000_000
    context = {'page_name': 'Main page',
               'app_name': 'Questoor',
               'user_count': user_count}
    return render(request, 'main_page/index.html',context)
