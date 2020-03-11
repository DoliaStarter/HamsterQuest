from django import forms


class QuestForm(forms.Form):
    quest_title = forms.CharField(label="Title")
    quest_description = forms.CharField(label="Description")
    player_amount = forms.CharField(label="Number of players")


class StageForm(forms.Form):
    stage_title = forms.CharField(label="Stage title")
    correct_answer = forms.CharField(label="Correct answer")
