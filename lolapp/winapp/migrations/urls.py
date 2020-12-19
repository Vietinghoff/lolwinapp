from django.urls import path
from . import views
from winapp import summoner_name_form

urlpatterns = [
    path('index/', views.index, name='index'),
    path('summoner/', summoner_name_form.submit_summoner_name, name='summoner name')
]