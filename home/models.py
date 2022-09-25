from asyncio import events
from dataclasses import field
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=20, null=True)
    rollno = models.CharField(max_length=15, null=True)
    department = models.CharField(max_length=100, null=True)
    degree = models.CharField(max_length=50, null=True)
    p_email = models.CharField(max_length=100, null=True)
    contact = models.CharField(max_length=15, null=True)

class Queries(models.Model):
    roll_no_ = models.AutoField(primary_key=True)
    event_ = models.CharField(max_length=100)
    questions_ = models.TextField()


class GroupMentoringTopics(models.Model):
    roll_no_ = models.AutoField(primary_key=True)
    topic_ = models.CharField(max_length=100)


class EventsAttending(models.Model):
    roll_no_ = models.AutoField(primary_key=True)
    beyond_the_horizon_ = models.BooleanField(default=False)
    workshop_1_ = models.BooleanField(default=False)
    workshop_2_ = models.BooleanField(default=False)
    workshop_3_ = models.BooleanField(default=False)
    workshop_4_ = models.BooleanField(default=False)
    workshop_5_ = models.BooleanField(default=False)
    workshop_6_ = models.BooleanField(default=False)
    standup_ = models.BooleanField(default=False)
    game_night_ = models.BooleanField(default=False)
    student_alumni_mentorship_ = models.BooleanField(default=False)
    coming_full_circle_ = models.BooleanField(default=False)
    ypo_ = models.BooleanField(default=False)
    tedx_ = models.BooleanField(default=False)
    ceo_connect_ = models.BooleanField(default=False)
    speed_mentoring_ = models.BooleanField(default=False)

    
class mi_gd(models.Model):
    mode = models.CharField(default=False, max_length=100)
    pref1 = models.CharField(default=False, max_length=100)
    pref2 = models.CharField(default=False, max_length=100)
    pref3 = models.CharField(default=False, max_length=100)
    date = models.CharField(default=False, max_length=100)
    resume = models.FileField(upload_to='resume', blank=True)