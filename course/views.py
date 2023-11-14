from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.generics import (CreateAPIView, ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import IsAuthenticated

from permissions import IsITAdminOrIsEducationalAssistant

from .models import *
from .serializers import *


class ApprovedCourseViewSet(viewsets.ModelViewSet):
    queryset = ApprovedCourse.objects.all()
    serializer_class = ApprovedCourseSerializer


class SemesterCourseAPICreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsITAdminOrIsEducationalAssistant]
    queryset = SemesterCourse.objects.all()
    serializer_class = SemesterCourseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SemesterCourseFilterSet

    def get_permissions(self):
        if self.request.method == "POST":
            return [permission() for permission in self.permission_classes]
        return []


class SemesterRUD(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsITAdminOrIsEducationalAssistant]
    queryset = SemesterCourse.objects.all()
    serializer_class = SemesterCourseSerializer

    def get_permissions(self):
        if self.request.method in ["PUT", "DELETE"]:
            return [permission() for permission in self.permission_classes]
        return []
