from django.db import models

class champs(models.Model):
    champ_name = models.CharField(max_length=100)
    champ_splitpush = models.IntegerField()
    champ_pick = models.IntegerField()
    champ_siege = models.IntegerField()
    champ_control = models.IntegerField()
    champ_teamfight = models.IntegerField()
    
    def __str__(self):
        return self.champ_name