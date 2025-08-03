from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WorkoutLogViewSet, MealLogViewSet

router = DefaultRouter()
router.register(r'workouts', WorkoutLogViewSet)
router.register(r'meals', MealLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
