from django.db import models
from django.utils import timezone 

class WorkoutLog(models.Model):
    date = models.DateField()
    type = models.CharField(max_length=100)
    duration = models.PositiveIntegerField(help_text="Duration in minutes")

    def __str__(self):
        return f"{self.date} - {self.type} ({self.duration} mins)"

class MealLog(models.Model):
    datetime = models.DateTimeField(default=timezone.now)  
    meal = models.CharField(max_length=100)
    calories = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.datetime} - {self.meal} ({self.calories} kcal)"
