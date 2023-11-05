from rest_framework.views import APIView
from user.models import Student
from user.serializer import StudentSerializer
from course.serializers import *
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class StudentPassCourseReport(APIView):
    def get(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        serializer = ApprovedCoueseSerializer(instance=student.passed_courses, many=True)
        return Response(serializer.data)
