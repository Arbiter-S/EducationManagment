from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from permissions import *
from .serializers import *
from .models import *
from user.models import *


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


class CourseListView(ListAPIView):
    # permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = StudentCourseReadSerializer

    def get_queryset(self):
        user_instance = self.request.user
        student_instance = Student.objects.get(pk=user_instance.pk)
        passing_courses = student_instance.passing_courses

        return passing_courses


class ExamsListView(ListAPIView):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = ExamsSerializer

    def get_queryset(self):
        user_instance = self.request.user
        student_instance = Student.objects.get(pk=user_instance.pk)
        passing_courses = student_instance.passing_courses

        return passing_courses
