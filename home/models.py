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
    roll_no = models.AutoField(primary_key=True)
    event = models.CharField(max_length=100)
    questions = models.TextField()


class GroupMentoringTopics(models.Model):
    roll_no = models.AutoField(primary_key=True)
    topic = models.CharField(max_length=100)


class EventsAttending(models.Model):
    roll_no = models.AutoField(primary_key=True)
    beyond_the_horizon = models.BooleanField(default=False)
    workshop_1 = models.BooleanField(default=False)
    workshop_2 = models.BooleanField(default=False)
    workshop_3 = models.BooleanField(default=False)
    workshop_4 = models.BooleanField(default=False)
    workshop_5 = models.BooleanField(default=False)
    workshop_6 = models.BooleanField(default=False)
    standup = models.BooleanField(default=False)
    game_night = models.BooleanField(default=False)
    student_alumni_mentorship = models.BooleanField(default=False)
    coming_full_circle = models.BooleanField(default=False)
    ypo = models.BooleanField(default=False)
    tedx = models.BooleanField(default=False)
    ceo_connect = models.BooleanField(default=False)
    speed_mentoring = models.BooleanField(default=False)

    
class mi_gd(models.Model):
    mode = models.CharField(default=False, max_length=100)
    pref1 = models.CharField(default=False, max_length=100)
    pref2 = models.CharField(default=False, max_length=100)
    pref3 = models.CharField(default=False, max_length=100)
    date = models.CharField(default=False, max_length=100)
    resume = models.FileField(upload_to='resume', blank=True)

class Event_url(models.Model):
    roll_no=models.PositiveBigIntegerField
    event=models.CharField(max_length=100)
    question=models.CharField(max_length=100)

