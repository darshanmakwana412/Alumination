from asyncio import events
from dataclasses import field
from django.db import models
from django.contrib.auth.models import User

# # Simple model for Events of Alumination
# class Event(models.Model):
#     id_ = models.AutoField(primary_key=True)
#     name_ = models.CharField(max_length=100)

#     # Add more fields about the Events

#     def __str__(self):
#         return self.name_

# # Hierarchical Model for user profiles
# class Profile(models.Model):
#     user_ = models.OneToOneField(User, on_delete=models.CASCADE)
#     name_ = models.CharField(max_length=100)
#     events_ = models.ManyToManyField(Event, related_name='events')

#     # Add more fields about the Profile using the website

#     def __str__(self):
#         return self.name_

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