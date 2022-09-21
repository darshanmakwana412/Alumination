from asyncio import events
from dataclasses import field
from django.db import models
from django.contrib.auth.models import User

# Simple model for Events of Alumination
class Event(models.Model):
    id_ = models.AutoField(primary_key=True)
    name_ = models.CharField(max_length=100)

    # Add more fields about the Events

    def __str__(self):
        return self.name_

# Hierarchical Model for user profiles
class Profile(models.Model):
    user_ = models.OneToOneField(User, on_delete=models.CASCADE)
    name_ = models.CharField(max_length=100)
    events_ = models.ManyToManyField(Event, related_name='events')

    # Add more fields about the Profile using the website

    def __str__(self):
        return self.name_