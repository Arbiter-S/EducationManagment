from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
import jdatetime
from django.db import transaction
from course.serializers import *
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from permissions import *
from .serializer import *


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


class StudentRemainingTerms(APIView):
    permission_classes = [IsAuthenticated, IsITAdminOrIsStudent]

    def get(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        fall_semester = 0
        spring_semester = 0
        if 7 <= jdatetime.date.today().month < 11:
            fall_semester = 1
        else:
            spring_semester = 2

        sum_of_semester = ((jdatetime.date.today().year - int(student.entry_year)) * 2) + max(fall_semester,
                                                                                              spring_semester)

        return Response({"remain semester": student.academic_terms - sum_of_semester})


class CreateRegisterCourse(ListCreateAPIView):
    queryset = UnitRegisterRequest.objects.all()
    serializer_class = UnitRegisterRequestSerializer

    # permission_classes =

    def perform_create(self, serializer):
        student = self.get_student()
        serializer.save(student=student)

    def get_student(self):
        return get_object_or_404(Student, pk=self.kwargs['pk'])


class SubmitRegisterCourse(APIView):
    @transaction.atomic
    def post(self, request, pk):
        pass
        # Check if the prerequisite course is in an accepted state
