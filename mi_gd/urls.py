from django.urls import path
from . import views

urlpatterns = [
    path('mi_gd/', views.migd, name="mi_gd"),
]