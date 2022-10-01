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
    date = models.DateTimeField()


class EventsAttending(models.Model):
    roll_no = models.AutoField(primary_key=True)                        #1
    beyond_the_horizon = models.BooleanField(default=False)             #2
    it_software = models.BooleanField(default=False)                     #3
    consulting = models.BooleanField(default=False)                     #4
    analytics = models.BooleanField(default=False)                     #5
    quant = models.BooleanField(default=False)                     #6    
    hr = models.BooleanField(default=False)                     #7
    product_management = models.BooleanField(default=False)                     #8
    standup = models.BooleanField(default=False)                        #9
    game_night = models.BooleanField(default=False)                     #10
    student_alumni_mentorship = models.BooleanField(default=False)      #11
    coming_full_circle = models.BooleanField(default=False)             #12
    ypo = models.BooleanField(default=False)                            #13
    tedx = models.BooleanField(default=False)                           #14
    ceo_connect = models.BooleanField(default=False)                    #15
    speed_mentoring = models.BooleanField(default=False)                #16

    
class mi_gd(models.Model):
    mode = models.CharField(default=False, max_length=100)
    pref1 = models.CharField(default=False, max_length=100)
    pref2 = models.CharField(default=False, max_length=100)
    pref3 = models.CharField(default=False, max_length=100)
    date = models.CharField(default=False, max_length=100)
    resume = models.FileField(upload_to='resume', blank=True)

# question taken for 
class feedback_question(models.Model):
    feedback_question=models.CharField(max_length=100)
    
class Event_url(models.Model):
    roll_no=models.PositiveBigIntegerField
    event=models.CharField(max_length=100)
    question=models.CharField(max_length=100)