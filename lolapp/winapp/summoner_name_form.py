from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .cass_api import get_match, get_champions

REGION_CHOICES=[
    ('NA', 'North America'),
    ('EU', 'Europe'),
]
#sets up the current django form object with a place to put your name and a selection for a region. 
#ADD MORE REGIONS BEFORE RELEASE - Justin
class summoner_name_form(forms.Form):
    summoner_name = forms.CharField(max_length=100, label='Summoner Name')
    region_name = forms.CharField(label='Region', widget=forms.Select(choices=REGION_CHOICES))

#if the form is filled in correctly, it will go to the "submitted" URL which will show game info.
#otherwise it will just bring you back to the form and tell you what you did incorrectly. 
#TEST THIS AND MAKE SURE THAT NO SENSITIVE INFO IS GIVEN DURING INCORRECT INPUTS - Justin
def submit_summoner_name(request):
    submitted = False
    if request.method == 'POST':
        form = summoner_name_form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            match = get_match(cd['summoner_name'],cd['region_name'])
            champ = get_champions(match)
            submitted = True
            return render(request,
            'summoner_name_form.html',
            {'form': form, 'submitted': submitted, 'cd':cd, 'match':match, 'champ':champ})
    else:
        form = summoner_name_form()
        if 'submitted' in request.GET:
            submitted = True
        
    return render(request, 
        'summoner_name_form.html',
        {'form': form, 'submitted': submitted}
        )            