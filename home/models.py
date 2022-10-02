<<<<<<< HEAD
=======
from atexit import register
from email.mime import image
>>>>>>> 8719d07f1d9c4a70c7f2579312b89c1e3f5d6280
from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# class Event(models.Model):
#     id
#     name = models.TextField(default="Friendly Funeral")
#     description = models.TextField(default="Ops!! Looks Like this event is not finalised, we will updating soon")
#     image = models.ImageField()
#     registered = models.BooleanField(default=False)
#     models.DateTimeField(auto_now = True)

#     def __str__(self):
#         return self.name

<<<<<<< HEAD
class migd(models.Model):
    rollno = models.CharField(primary_key=True, max_length=9)
    dateTime = models.DateTimeField(auto_now=True)
    interest = models.CharField(default='', max_length=100)
    pref1 = models.CharField(default='', max_length=100)
    pref2 = models.CharField(default='', max_length=100)
    pref3 = models.CharField(default='', max_length=100)
    dateAvailable = models.CharField(default='', max_length=100)
    coreField = models.CharField(default='', max_length=100)
    resume = models.FileField(upload_to='resume', blank=True)

class shadowPrograme(models.Model):
    rollno = models.CharField(primary_key=True, max_length=50)
    dateTime = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='paymentProof', blank=True)

=======
>>>>>>> 8719d07f1d9c4a70c7f2579312b89c1e3f5d6280
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=20, null=True)
    rollno = models.CharField(max_length=15, null=True)
    department = models.CharField(max_length=100, null=True)
    degree = models.CharField(max_length=50, null=True)
    p_email = models.CharField(max_length=100, null=True)
    contact = models.CharField(max_length=15, null=True)
    # events = models.ManyToManyField(Event, related_name='attendees')

    def __str__(self):
        return self.name


class Queries(models.Model):
    roll_no = models.AutoField(primary_key=True)
    event = models.CharField(max_length=100)
    questions = models.TextField()


class GroupMentoringTopics(models.Model):
    roll_no = models.AutoField(primary_key=True)
    topic = models.CharField(max_length=100)
    dateTime = models.DateTimeField(auto_now=True)

 
class EventsAttending(models.Model):
<<<<<<< HEAD
    roll_no = models.CharField(primary_key=True, max_length=9)                        #1
=======
    roll_no = models.AutoField(primary_key=True)                        #1
>>>>>>> 8719d07f1d9c4a70c7f2579312b89c1e3f5d6280
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

class speedMentoring(models.Model):
    date = models.CharField(default=False, max_length=100)
    pref1 = models.CharField(default=False, max_length=100)
    pref2 = models.CharField(default=False, max_length=100)

class groupm(models.Model):
    date = models.CharField(default=False, max_length=100)
    pref1 = models.CharField(default=False, max_length=100)
    pref2 = models.CharField(default=False, max_length=100)

# question taken for 
class feedback_question(models.Model):
    feedback_question=models.CharField(max_length=100)
    
class Event_url(models.Model):
    roll_no=models.PositiveBigIntegerField
    event=models.CharField(max_length=100)
    question=models.CharField(max_length=100)