from django.urls import path
from .views import *

urlpatterns = [
    path("student/<str:pk>/passed-courses/", StudentPassedCourseReport.as_view(), name='pass_course_report'),
    path("student/<str:pk>/passing-courses/", StudentPassingCourseReport.as_view(), name="passing_course"),

]
