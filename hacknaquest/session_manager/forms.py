from django import forms
from django.contrib.auth.models import User
import json

DATA = {
    'quest_title': 'cool quest',
    'quest_description': 'Lorem ipsum dolor',
    'author': 'A writer',
    'stages': {
        'stage1': {
            'task': 'The export statement is used when creating JavaScript modules to export functions, objects, or primitive values from the module so they can be used by other programs with the import statement.Exported modules are in strict mode whether you declare them as such or not. The export statement cannot be used in embedded scripts.The export statement is used when creating JavaScript modules to export functions, objects, or primitive values from the module so they can be used by other programs with the import statement.Exported modules are in strict mode whether you declare them as such or not. The export statement cannot be used in embedded scripts.The export statement is used when creating JavaScript modules to export functions, objects, or primitive values from the module so they can be used by other programs with the import statement.Exported modules are in strict mode whether you declare them as such or not. The export statement cannot be used in embedded scripts.The export statement is used when creating JavaScript modules to export functions, objects, or primitive values from the module so they can be used by other programs with the import statement.Exported modules are in strict mode whether you declare them as such or not. The export statement cannot be used in embedded scripts.The export statement is used when creating JavaScript modules to export functions, objects, or primitive values from the module so they can be used by other programs with the import statement.Exported modules are in strict mode whether you declare them as such or not. The export statement cannot be used in embedded scripts.The export statement is used when creating JavaScript modules to export functions, objects, or primitive values from the module so they can be used by other programs with the import statement.Exported modules are in strict mode whether you declare them as such or not. The export statement cannot be used in embedded scripts.',
            'location': '12.0444404;12.4564888',
            'status': 'actual queststate', 
            'is_completed': 'False',
            'answers': {
                '42': 'stage2',
                'answer': 'stage3',
            }
        },
        'stage2': {
            'task': 'some task for stage 2',
            'location': 'location',
            'status': 'status',
            'is_completed': 'False',
            'answers': {
                '10': "stage1",
                '23': 'null'
            }
        },
        'stage3': {
            'task': 'some task for stage 3',
            'location': 'location',
            'status': 'status',
            'is_completed': 'False',
            'answers': {
                '10': 'stage1',
                '11': 'null'
            }
        }
    }
}




class SessionManagerMainForm(forms.Form):
    # widget=forms.ImageField(attrs={'id': 'photo'}))
    photo = forms.ImageField(label='', required=False)
    answer = forms.CharField(label='', required=False,
                             max_length=100,
                             widget=forms.TextInput(attrs={'id': 'answer', 'placeholder': 'Answer...'}))

def makeJSON():
    tmp_DATA = json.dumps(DATA, separators=(',', ':'))
    my_json = json.loads(tmp_DATA)
    return my_json


def getKey():
    key = zip(list(DATA["stages"].keys()), list(DATA["stages"].keys()))
    keys = list(key)
    return keys

class RadioStages(forms.Form):
    STAGES = getKey()
    buttons = forms.CharField(label='', initial='stage1', widget=forms.RadioSelect(choices=STAGES))