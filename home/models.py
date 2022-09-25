from asyncio import events
from dataclasses import field
from django.db import models
from django.contrib.auth.models import User

# Simple model for Events of Alumination
class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    # Add more fields about the Events

    def __str__(self):
        return self.name_

# Hierarchical Model for user profiles
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    events = models.ManyToManyField(Event, related_name='events')

    # Add more fields about the Profile using the website

    def __str__(self):
        return self.name_

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