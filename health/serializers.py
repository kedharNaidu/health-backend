from rest_framework import serializers
from .models import WorkoutLog, MealLog

class WorkoutLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutLog
        fields = '__all__'

class MealLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealLog
        fields = '__all__'
