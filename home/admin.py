from django.contrib import admin
from .models import Queries, GroupMentoringTopics, EventsAttending

admin.site.register(Queries, admin)
admin.site.register(GroupMentoringTopics, admin)
admin.site.register(EventsAttending, admin)