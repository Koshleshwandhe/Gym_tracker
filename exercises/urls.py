from django.urls import path
from . import views

urlpatterns = [
    path('', views.exercise_view, name='exercise'),
    path('all_exercises/', views.all_exercises_view, name='all_exercises'),
]