from django.urls import path

from .views import *

urlpatterns = [
    path("admin/faculties/", FacultyAPIListView.as_view(), name = "facultyListView"),
    path("admin/faculties/<int:pk>/", FacultyAPIDetailView.as_view(), name = "facultyDetailView"),   
]