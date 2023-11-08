from django.urls import path
from .views import *

urlpatterns = [
    path("student/<str:pk>/passed-courses/", StudentPassedCourseReport.as_view(), name='pass_course_report'),
    path("student/<str:pk>/passing-courses/", StudentPassingCourseReport.as_view(), name="passing_course"),
    path("student/<str:pk>/remaining-terms/", StudentRemainingTerms.as_view(), name="remaining_terms"),
    path("student/<str:pk>/course-selection/create/", CreateRegisterCourse.as_view(), name='create_register_course'),
    path("student/<str:pk>/course-selection/submit/", SubmitRegisterCourse.as_view(), name="submit_course_selection"),
]
