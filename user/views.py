from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import *
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken

from .models import *

from .serializer import *

class StudentCreateListAPIView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = StudentFilterSet

class StudentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class ProfessorAPIListView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class ProfessorAPIDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class EducationalAssistantAPIListView(ListCreateAPIView):
    queryset = EducationalAssistant.objects.all()
    serializer_class = EducationalAssistantSerializer
    
class EducationalAssistantAPIDetailView(RetrieveUpdateDestroyAPIView):
    queryset = EducationalAssistant.objects.all()
    serializer_class = EducationalAssistantSerializer

