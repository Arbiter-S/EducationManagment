from rest_framework.generics import *
from rest_framework.permissions import IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend

from permissions import *


from .serializer import *

class StudentListAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsITAdmin]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = StudentFilterSet

class StudentAPIDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsITAdmin]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class ProfessorAPIListView(ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsITAdmin]
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class ProfessorAPIDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsITAdmin]
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class EducationalAssistantAPIListView(ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsITAdmin]
    queryset = EducationalAssistant.objects.all()
    serializer_class = EducationalAssistantSerializer
    
class EducationalAssistantAPIDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsITAdmin]
    queryset = EducationalAssistant.objects.all()
    serializer_class = EducationalAssistantSerializer