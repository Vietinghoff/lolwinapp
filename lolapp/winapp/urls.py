from django.urls import path
from winapp import summoner_name_form

urlpatterns = [
    path('summoner/', summoner_name_form.submit_summoner_name, name='summoner name'),
]