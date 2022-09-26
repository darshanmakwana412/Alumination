from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('login/', views.loginView, name="login"),
    path('register/', views.registerView, name='register'),
    path('logout', views.logoutView, name="logout"),
    path('profile/', views.profile, name="profile"),
    path('mi_gd', views.migd, name="migd"),
    path('', views.teamPage, name="teampage"),
]