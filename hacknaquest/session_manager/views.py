from django.shortcuts import render
from django.http import HttpResponse
from session_manager.forms import SessionManagerMainForm, RadioStages
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from json import loads


# Create your views here.

DATA = {
    "quest_title": ["cool quest"],
    "quest_description": ["Lorem ipsum dolor sit amet,consectetur adipiscing elit. Pellentesque lectus mi, mollis id tincidunt ac, mattis sed magna. Nullam euismod quam eu auctor sodales. Fusce libero tortor, vulputate sit amet euismod sed, commodo nec justo. Nam sodales tortor in ex fermentum, in semper nisl lobortis. Ut elementum tristique velit at fermentum. Quisque eu eros egestas, placerat enim non, laoreet ex. Interdum et malesuada fames ac ante ipsum primis in faucibus. Integer sit amet hendrerit turpis. "],
    "author": ["A writer"],
    "stages": [
        "stage1": [
            "task": ["some task"],
            "location": ["12.0444404;12.4564888"],
            "status": ["actual queststate"], 
            "is_completed": [False],
            "answers": [
                "42": ["stage2"],
                "answer": ["stage3"],
            ]
        ],
        "stage2": [
            "task": ["task"],
            "location": ["location"],
            "status": ["status"],
            "is_completed": [False],
            "answers": [
                "10": ["stage1"],
                "23": [null]
            ]
        ],
        "stage3": [
            "task": ["task"],
            "location": ["location"],
            "status": ["status"],
            "is_completed": [False],
            "answers": [
                "10": ["stage1"],
                "11": [null]
            ]
        ]
    ]
}

def index(request):
    json_dump = json.dumps(DATA)
    form = SessionManagerMainForm()
    radio_stages = RadioStages()
    keys = zip(json_dump["stages"].keys(), data["stages"].keys())
    keys = list(keys)
    radio_stages.STAGES = keys
    context = {
        'page_name': "Session manager",
        'form': form,
        'radio_stages': radio_stages
    }
    return render(request, 'session_manager/index.html', context)


@csrf_exempt
def get_answer(request):
    return HttpResponse(status=200)

@csrf_exempt
def get_data(request) -> dict:
    """Returns data about quest in session."""
    data = loads(request.body)
    keys = zip(data.keys(), data.keys())
    keys = list(keys)
    radio_stages.STAGES = keys
    return HttpResponse(status=200)

def save_data(request) -> None:
    """Save user progress"""
    pass
