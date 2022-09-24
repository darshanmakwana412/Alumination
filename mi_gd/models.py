from fileinput import filename
from django.db import models

# Create your models here.
class mi_gd(models.Model):
    mode = models.CharField(default=False, max_length=100)
    pref1 = models.CharField(default=False, max_length=100)
    pref2 = models.CharField(default=False, max_length=100)
    pref3 = models.CharField(default=False, max_length=100)
    date = models.CharField(default=False, max_length=100)
    resume = models.FileField(upload_to='resume', blank=True)
