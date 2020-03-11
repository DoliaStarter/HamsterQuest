from django.shortcuts import render
from django.http import HttpResponse
from main.forms import SessionManagerMainForm


# Create your views here.


def index(request):
    if request.method == 'POST':
        form = SessionManagerMainForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = SessionManagerMainForm()        
    
    context = {
        'page_name': "Session manager",
        'form': form, 
    }

    return render(request, 'session_manager/index.html', context)

