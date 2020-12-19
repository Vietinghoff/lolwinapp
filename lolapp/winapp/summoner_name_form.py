from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect

REGION_CHOICES=[
    ('NA', 'North America'),
    ('EU', 'Europe'),
]

class summoner_name_form(forms.Form):
    summoner_name = forms.CharField(max_length=100, label='Summoner Name')
    region_name = forms.CharField(label='Region', widget=forms.Select(choices=REGION_CHOICES))


def submit_summoner_name(request):
    submitted = False
    if request.method == 'POST':
        form = summoner_name_form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            assert False
            return HttpResponseRedirect('/summoner?submitted=True')
    else:
        form = summoner_name_form()
        if 'submitted' in request.GET:
            submitted = True
        
    return render(request, 
        'summoner_name_form.html',
        {'form': form, 'submitted': submitted}
        )            