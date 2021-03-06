# coding: utf-8

from django import forms
from .models import TEAM_STATUS, PLAYER_STATUS

class LineupAddForm(forms.Form):

    match_id = forms.CharField(required=True)
    team_id = forms.CharField(required=True)
    team_status = forms.ChoiceField(required=True, choices=TEAM_STATUS)
    player_name = forms.CharField(required=True)
    player_number = forms.CharField(required=False)
    player_position = forms.CharField(required=False)
    player_status = forms.ChoiceField(required=True, choices=PLAYER_STATUS)
    order = forms.CharField(required=False)

class LineupEditForm(forms.Form):
    lineup_id = forms.CharField(required=True)
    match_id = forms.CharField(required=False)
    team_id = forms.CharField(required=False)
    team_status = forms.ChoiceField(choices=TEAM_STATUS, required=False)
    player_name = forms.CharField(required=True)
    player_number = forms.CharField(required=False)
    player_position = forms.CharField(required=False)
    player_status = forms.ChoiceField(required=True, choices=PLAYER_STATUS)
    order = forms.CharField(required=False)
    

