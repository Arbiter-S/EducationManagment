from django.urls import path
from rest_framework_simplejwt.views import (TokenBlacklistView,
                                            TokenObtainPairView,
                                            TokenRefreshView)

from .views import *

urlpatterns = [
    path("users/login/", TokenObtainPairView.as_view(), name="TokenCreate"),
    path("users/login-refresh/", TokenRefreshView.as_view(), name="TokenRefresh"),
    path("users/logout/", TokenBlacklistView.as_view(), name="TokenBlacklist"),
    path("admin/students/", StudentListAPIView.as_view(), name="StudentList"),
    path("admin/student/<str:pk>/", StudentAPIDetailView.as_view(), name="StudentDetail"),
    path("admin/professor/", ProfessorAPIListView.as_view(), name = "ProfessorListView"),
    path("admin/professor/<str:pk>/", ProfessorAPIDetailView.as_view(), name = "ProfessorDetailView"),
    path("admin/assistant/", EducationalAssistantAPIListView.as_view(), name = "EducationalAssistantListView"),
    path("admin/assistant/<str:pk>/", EducationalAssistantAPIDetailView.as_view(), name = "EducationalAssistantDetailView"),
    path("students/", EducationalAssistantStudentAPIListView.as_view(), name="EducationalAssistantStudentsList"),
    path("students/<str:pk>", EducationalAssistantStudentAPIRetrieveView.as_view(), name="EducationalAssistantStudentsRetrieve"),
    path("professors/", EducationalAssistantProfessorAPIListView.as_view(), name="EducationalAssistantProfessorList"),
    path("professors/<str:pk>", EducationalAssistantProfessorAPIRetrieveView.as_view(), name="EducationalAssistantProfessorRetrieve"),
    path("users/profile/<str:pk>", UserProfileUpdate.as_view(), name="ProfileUpdate")
]