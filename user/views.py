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
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProfessorFilterSet


class ProfessorAPIDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsITAdmin]
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


class EducationalAssistantAPIListView(ListCreateAPIView):
    # permission_classes = [IsAuthenticated, IsITAdmin]
    queryset = EducationalAssistant.objects.all()
    serializer_class = EducationalAssistantSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EducationalAssistantFilterSet


class EducationalAssistantAPIDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsITAdmin]
    queryset = EducationalAssistant.objects.all()
    serializer_class = EducationalAssistantSerializer


class EducationalAssistantStudentAPIListView(ListAPIView):
    permission_classes = [IsAuthenticated, IsAssistant]
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = StudentFilterSet

    def get_queryset(self):
        assistant = EducationalAssistant.objects.get(pk=self.request.user.pk)
        queryset = Student.objects.filter(department=assistant.department)

        return queryset


class EducationalAssistantStudentAPIRetrieveView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, IsAssistant]

    def get_queryset(self):
        assistant = EducationalAssistant.objects.get(pk=self.request.user.pk)
        queryset = Student.objects.filter(department=assistant.department)

        return queryset

    def get_serializer_class(self):
        if self.request.method == "GET":
            return StudentSerializer

        elif self.request.method in ["PUT", "PATCH"]:
            return StudentUpdateSerializer


class EducationalAssistantProfessorAPIListView(ListAPIView):
    permission_classes = [IsAuthenticated, IsAssistant]
    serializer_class = ProfessorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProfessorFilterSet

    def get_queryset(self):
        assistant = EducationalAssistant.objects.get(pk=self.request.user.pk)
        queryset = Professor.objects.filter(department=assistant.department)

        return queryset


class EducationalAssistantProfessorAPIRetrieveView(RetrieveAPIView):
    permission_classes = [IsAuthenticated, IsAssistant]
    serializer_class = ProfessorSerializer

    def get_queryset(self):
        assistant = EducationalAssistant.objects.get(pk=self.request.user.pk)
        queryset = Professor.objects.filter(department=assistant.department)

        return queryset


class UserProfileUpdate(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, IsOwner]
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return UserReadSerializer

        elif self.request.method in ["PUT", "PATCH"]:
            return UserUpdateSerializer



