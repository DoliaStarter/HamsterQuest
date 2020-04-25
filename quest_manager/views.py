from django.shortcuts import render
from .forms import QuestForm, StageForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from main.models import *

from json import loads
# Create your views here.


def index(request):
    context = {
        'page_name': 'Quest manager',
        'quest_form': QuestForm(),
        'stage_form': StageForm()
    }
    return render(request, 'quest_manager/index.html', context)


def create_stage(data, quest,):  # TO BE MODIFIED!!!!!!!  NEW FORMAT OF !!!!!!!!

    stage_id = data['stage_id']
    stage_title = data['stage_title']
    stage_task = data['stage_task']
    correct_answer = data['correct_answer']
    # MUST BE PARSED TO INT AND LINKED TO STAGE IN THE FUTURE!!!!
    stage_location = data["stage_location"]
    previous_stage_id = data['previous_stage_id']
    children = data['children']

    if previous_stage_id != None:
        prev = Stages.objects.get(quest_id=quest, title=previous_stage_id)
    else:
        prev = None

    try:
        # type_of_answer must be dynamic!!!
        stage = Stages.objects.get(
            quest_id=quest, previous_stage=prev, title=stage_id, type_of_answer="string")
        print("modifying existing node")
    except Stages.DoesNotExist:
        if prev != None:
            # type_of_answer must be dynamic!!!
            stage = Stages(quest_id=quest, title=stage_id,
                           type_of_answer="string")
            stage.previous_stage = prev
        else:
            # type_of_answer must be dynamic!!!
            stage = Stages(quest_id=quest, title=stage_id,
                           type_of_answer="string")
        print("created node")

    modified = [stage_id]
    stage.title = stage_title
    stage.task = stage_task
    stage.answer = correct_answer
    stage.save()
    for child in children:
        print("Апасна рикурсия")
        modified.extend(create_stage(child, quest))

    return modified


@csrf_exempt
def create_quest(request):
    if (not request.user.is_authenticated):
        print("попытка взлома так сказатб")
        return  # кибербезопасноть так сказатб

    data = loads(request.body)
    print(data)
    quest_id = data['quest_id']
    quest_data = data['quest_data']
    title = quest_data['quest_title']
    description = quest_data['quest_description']
    player_amount = quest_data['player_amount']

    user = request.user
    user_profile = UserProfile.objects.get(user=user)

    quest = None
    if (quest_id == None):
        quest = Quests(author_id=user_profile, title=title,
                       player_amount=player_amount, description=description)
        quest.save()
    else:
        try:
            quest = Quests.objects.get(id=quest_id, author_id=user_profile)
        except Quests.DoesNotExist:
            print(":( cant hack this ):")
            return HttpResponse(status=404)

    quest.description = description
    quest.title = title
    quest.player_amount = player_amount
    quest.save()

    ID_IN_DB = []
    for tmp in Stages.objects.all():
        if (tmp.quest_id == quest):
            ID_IN_DB.append(tmp.id)

    stages = data['stage_tree']
    modified = create_stage(stages, quest)

    to_delete = list(set(ID_IN_DB) - set(modified))

    for i in to_delete:
        print(i)
        instance = Stages.objects.get(id=i, quest_id=quest)
        instance.delete()
        print("deleted stage")

    return HttpResponse(status=200)


