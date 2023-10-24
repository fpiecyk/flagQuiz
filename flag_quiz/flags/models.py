from django.db import models


# Create your models here.

class FlagData(models.Model):
    full_name = models.CharField(('full_name'), max_length=100)
    short_name = models.CharField(('short_name'), max_length=2, primary_key=True)
    flag_img = models.CharField(('flag_img'), max_length=6)

