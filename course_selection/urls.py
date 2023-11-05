from django.urls import path
from .views import *

urlpatterns = [
    path("student/<str:pk>/pass-course-report/", StudentPassCourseReport.as_view(), name='pass_course_report'),

]
