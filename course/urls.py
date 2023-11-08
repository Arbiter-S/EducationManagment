from django.urls import include, path
from rest_framework import routers

from .views import *

subject_router = routers.DefaultRouter()
subject_router.register(r'subjects', ApprovedCourseViewSet, basename='survey')


urlpatterns = [
    path('', include(subject_router.urls)),
    path('courses/', SemesterCourseAPICreateView.as_view(), name='SemesterCreateList'),
    path('courses/<int:pk>', SemesterRUD.as_view(), name='SemesterRUD'),
]