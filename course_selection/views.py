from rest_framework.views import APIView
from user.models import Student
from course.serializers import *
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from permissions import IsITAdmin, IsITAdminOrIsEducationalAssistantOrIsSupervisor


class StudentPassedCourseReport(APIView):
    permission_classes = [IsAuthenticated, IsITAdminOrIsEducationalAssistantOrIsSupervisor]

    def get(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        serializer = ApprovedCourseSerializer(instance=student.passed_courses, many=True)
        return Response(serializer.data)


class StudentPassingCourseReport(APIView):
    permission_classes = [IsAuthenticated, IsITAdminOrIsEducationalAssistantOrIsSupervisor]

    def get(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        serializer = SemesterCourseSerializer(instance=student.passing_courses, many=True)
        return Response(serializer.data)
