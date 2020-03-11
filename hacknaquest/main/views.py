from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm, SignInForm
from .models import UserProfile

# Create your views here.


def index(request):
    # later it will be a request to database.
    user_count = 1_000_000
    context = {'page_name': 'Main page',
               'app_name': 'Questoor',
               'user_count': user_count}
    return render(request, 'main_page/index.html', context)


def register(request):

    context = {'form': RegistrationForm(),
               'action': request.build_absolute_uri()}
    print(context)
    if request.method == 'POST':
        user_form = RegistrationForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            user_profile = UserProfile()
            user_profile.author_rating = 0
            user_profile.player_rating = 0
            user_profile.user = user
            user_profile.save()

            return HttpResponseRedirect('user_cabinet/')
        else:
            print(user_form.errors)
    return render(request, 'main_page/authentification.html', context)


def sign_in(request):
    failed = False
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if request.method == 'POST':
            username = request.POST['login']
            password = request.POST['password']
            # Use Django's machinery to attempt to see if the username/password
            # combination is valid - a User object is returned if it is.
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('user_cabinet/')
            else:
                print("так сказатб парольб неправельный")
                return HttpResponse("Invalid login details supplied.")
    context = {'form': SignInForm(),
               'action': request.build_absolute_uri(),
               'failed': failed}
    return render(request, 'main_page/authentification.html', context)
