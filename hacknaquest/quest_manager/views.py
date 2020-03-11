from django.shortcuts import render
from .forms import QuestForm, StageForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from json import loads
# Create your views here.


def index(request):
    context = {
        'page_name': 'Quest manager',
        'quest_form': QuestForm(),
        'stage_form': StageForm()
    }
    return render(request, 'quest_manager/index.html', context)

@csrf_exempt
def create_quest(request):
    data = loads(request.body)
    print(data)
    return HttpResponse(status=200)
