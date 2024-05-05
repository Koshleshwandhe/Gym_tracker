from django.db import models
from django.contrib.auth.models import User


class Exercise(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)    
    duration = models.FloatField()
    exercise_name = models.CharField(max_length=100)
    sets = models.IntegerField()
    reps = models.IntegerField()
    date_time = models.DateTimeField(auto_now_add=True,)