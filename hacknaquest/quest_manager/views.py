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

def create_stage(id,quest,all_stages):   #TO BE MODIFIED!!!!!!!  NEW FORMAT OF !!!!!!!!
    stage_data=None
    for i in all_stages:
        if i['stage_id']==id:
            stage_data=i
            break
    if stage_data==None:
        print("ERROR, cannot find quest with specified id in dictionary")
        return 
    stage_id=stage_data['stage_id']
    stage_title=stage_data['stage_title']
    stage_task=stage_data['stage_task']
    correct_answer=stage_data['correct_answer']
    stage_location=stage_data["stage_location"]   #MUST BE PARSED TO INT AND LINKED TO STAGE IN THE FUTURE!!!!
    previous_stage_id=stage_data['previous_stage_id']
    children=stage_data['children']
    
 
    if previous_stage_id!=None:
         prev =Stages.objects.get(quest_id=quest,id=previous_stage_id)    
    else:
        prev=None

    try:
        stage=Stages.objects.get(quest_id=quest,previous_stage=prev,id=stage_id,type_of_answer="string") #type_of_answer must be dynamic!!!
        print("modifying existing node")
    except Stages.DoesNotExist:
        stage=Stages(quest_id=quest,previous_stage=prev,id=stage_id,type_of_answer="string") #type_of_answer must be dynamic!!!
        print("created node")

    stage.title=stage_title
    stage.task=stage_task
    stage.answer=correct_answer            
    stage.save()
   
    mega_children=[]    # to be deleted
    for child in children:
       print("started recurent task #"+str(i))
       mega_children.extend(create_stage(child,quest,all_stages))
    return children




@csrf_exempt
def create_quest(request):
    if ( not request.user.is_authenticated): return   #кибербезопасноть так сказатб
    
    data = loads(request.body)

    quest_id=data['quest_id']
    username=data['creator']
    quest_data=data['quest_data']

    stages_data=data['stage_data']

    title=quest_data['quest_title']
    description=quest_data['quest_description']
    player_amount=quest_data['player_amount']
    

    user = request.user
    user_profile=UserProfile.objects.get(user=user)
     
      
    quest=None
    if (quest_id==None):
        quest=Quests(author_id=user_profile,title=title,player_amount=player_amount,description=description)
        quest.save()
    else:
        try:
          quest=Quests.objects.get(id=quest_id,author_id=user_profile)
        except Quests.DoesNotExist:
             print(":( cant hack this ):")
             return HttpResponse(status=404)
     
    quest.description=description
    quest.title=title
    quest.player_amount=player_amount
    quest.save()

    ID_IN_DB=[]
    for tmp in Stages.objects.all():
        if (tmp.quest_id==quest):
             ID_IN_DB.append(tmp.id)
    

    modified=[]
    
    for tmp in stages_data:    #SEND ID OF ROOOOOOOT !!!!!!! for optimissation
        
        if tmp['previous_stage_id']==None:
            modified.extend(create_stage(tmp['stage_id'],quest,stages_data))
            modified.append(tmp['stage_id'])
   
    
    for tmp in stages_data:
        if tmp['previous_stage_id']!=None and tmp['stage_id'] not in modified:
           modified.extend(create_stage(tmp['stage_id'],quest,stages_data))
           modified.append(tmp['stage_id'])

    print(ID_IN_DB)
    to_delete= list(set(ID_IN_DB) -set(modified))
    print(to_delete)
    for i in to_delete:
        print(i)
        instance = Stages.objects.get(id=i,quest_id=quest)
        instance.delete()
        print("deleted stage")

   
    return HttpResponse(status=200)
