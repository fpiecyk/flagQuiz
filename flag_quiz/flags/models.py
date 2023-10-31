from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class FlagData(models.Model):
    full_name = models.CharField(('full_name'), max_length=100)
    short_name = models.CharField(('short_name'), max_length=2, primary_key=True)
    flag_img = models.ImageField(upload_to="images/", blank=True)  

class ResultsData(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    player_score = models.IntegerField(blank=True)

    def __str__(self):
        return f'{self.player.username}'