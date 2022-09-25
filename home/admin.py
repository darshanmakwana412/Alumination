from django.contrib import admin
from .models import Queries, GroupMentoringTopics, EventsAttending

admin.site.register(Queries)
admin.site.register(GroupMentoringTopics)
admin.site.register(EventsAttending)