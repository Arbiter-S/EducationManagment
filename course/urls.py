from django.urls import path, include
from rest_framework import routers
from .views import ApprovedCourseViewSet

subject_router = routers.DefaultRouter()
subject_router.register(r'subjects', ApprovedCourseViewSet, basename='survey')


urlpatterns = [
    path('', include(subject_router.urls)),
]