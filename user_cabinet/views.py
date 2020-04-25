from django.shortcuts import render
from main.models import Quests


def index(request):
    username = request.user.get_username()
    context = {'page_name': 'User cabinet', 'username': username}
    return render(request, 'user_cabinet/index.html', context)


def search_quests(request):
    # TODO replace search in quests with search in Sessions
    username = request.user.get_username()
    quests = Quests.objects.order_by('title')
    context =  {'page_name': 'Search Quests', 'quests': quests, 'username': username}
    return render(request, 'user_cabinet/search_quests.html', context)


def user_quests(request):
    username = request.user.get_username()
    quests = Quests.objects.filter(
        author_id__user__username=username).order_by('title')
    context = {'page_name': 'My quests', 'quests': quests, 'username': username}
    return render(request, 'user_cabinet/search_quests.html', context)


def quest_desription(request):
    # TODO Add template that will describe quest
    print('Returning quest to describe')
    # TMP placehloder
    username = request.user.get_username()
    context = {'page_name': 'My quests', 'quests': [], 'username': username}
    return render(request, 'user_cabinet/search_quests.html', context)
