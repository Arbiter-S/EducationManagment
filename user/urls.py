from django.urls import include, path
from . import views

urlpatterns = [
    path('assistant/', views.EducationalAssistantAPIListCreateView.as_view(), name='assistant_ListCreateView'),
    path('assistant/<str:pk>/', views.EducationalAssistantAPIDetailView.as_view(), name="assistant_DetailView"),
]