from django.shortcuts import render
from django.http import HttpResponse
from main.forms import SessionManagerMainForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from json import loads


# Create your views here.


def index(request):
    form = SessionManagerMainForm()        
    context = {
        'page_name': "Session manager",
        'form': form, 
    }

    return render(request, 'session_manager/index.html', context)

@csrf_exempt
def get_answer(request):
    data = loads(request.body)
    print(data)
    return HttpResponse(status=200)