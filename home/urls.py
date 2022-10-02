from django.urls import path
from . import views

urlpatterns = [
    path('shadowProgram/', views.shadowProgram, name="shadowProgram"),
    path('profile/', views.profile, name="profile"),
    path('index/', views.index, name="index"),
    path('login/', views.loginView, name="login"),
    path('register/', views.registerView, name='register'),
    path('logout', views.logoutView, name="logout"),
    path('profile/', views.profile, name="profile"),
    path('mi_gd/', views.mi_gd, name="mi_gd"),
    path('qna', views.event_url, name="qna"),
    path('beyond_the_horizon', views.bth, name="bth"),
    path('ceoConnect', views.ceoConnect, name="ceoConnect"),
    path('speedMentoring', views.speedMentoring, name="speedMentoring"),
    path('group_mentoring', views.group_mentoring, name="group_mentoring"),
    path('coming_full_circle', views.cfc, name="coming_full_circle"),
    path('game_night', views.game_night, name="game_night"),
    path('eventState/<event>/<state>', views.eventState, name="eventState"),
    path('', views.index, name="teampage"),
    path('events', views.events, name="events")
]