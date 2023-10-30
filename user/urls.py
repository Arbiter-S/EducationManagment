from django.urls import include, path

from .views import *

urlpatterns = [
    path("admin/professor/", ProfessorAPIListView.as_view(), name = "ProfessorListView"),
    path("admin/professor/<str:pk>/", ProfessorAPIDetailView.as_view(), name = "ProfessorDetailView"),
    path("admin/assistant/", EducationalAssistantAPIListView.as_view(), name = "EducationalAssistantListView"),
    path("admin/assistant/<str:pk>/", EducationalAssistantAPIDetailView.as_view(), name = "EducationalAssistantDetailView"),
]