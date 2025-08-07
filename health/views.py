from rest_framework import viewsets
from .models import WorkoutLog, MealLog
from .serializers import WorkoutLogSerializer, MealLogSerializer

class WorkoutLogViewSet(viewsets.ModelViewSet):
    queryset = WorkoutLog.objects.all().order_by('-date')
    serializer_class = WorkoutLogSerializer

class MealLogViewSet(viewsets.ModelViewSet):
    queryset = MealLog.objects.all().order_by('-datetime')

    serializer_class = MealLogSerializer
