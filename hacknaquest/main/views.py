from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import RegistrationForm, SignInForm


# Create your views here.

def index(request):
    # later it will be a request to database.
    user_count = 1_000_000
    context = {'page_name': 'Main page',
               'app_name': 'Questoor',
               'user_count': user_count}
    return render(request, 'main_page/index.html', context)


def register(request):
    if request.method == 'POST':
        return HttpResponseRedirect('user_cabinet/')

    context = {'form': RegistrationForm(),
               'action': request.build_absolute_uri()}

    return render(request, 'main_page/authentification.html', context)


def sign_in(request):
    failed = False
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if data['passwd'] == '123':
                return HttpResponseRedirect('user_cabinet/')
            else:
                failed = True
    context = {'form': SignInForm(),
               'action': request.build_absolute_uri(),
               'failed': failed}
    return render(request, 'main_page/authentification.html', context)
