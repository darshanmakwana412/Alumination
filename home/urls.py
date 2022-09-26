from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('login/', views.loginView, name="login"),
    path('register/', views.registerView, name='register'),
    path('logout', views.logoutView, name="logout"),
    path('profile/', views.profile, name="profile"),
    path('mi_gd', views.migd, name="migd"),
    path('qna', views.event_url, name="qna"),
    path('event_url/',views.event_url,name="event_url"),
    path('beyond_the_horizon', views.bth, name="bth"),
    path('eventState/<event>/<state>', views.eventState, name="eventState")
    path('', views.teamPage, name="teampage"),
]