import jdatetime
from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from course.serializers import *
from permissions import *
from course.serializers import ApprovedCourseSerializer, SemesterCourseSerializer
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


class CreateSubmitRegisterCourse(APIView):
    def get(self, request, pk):
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

        # Get the UnitRegisterRequest objects for the specific student
        unit_register_requests = UnitRegisterRequest.objects.filter(student=student)

        # Serialize the data
        serializer = UnitRegisterRequestSerializer(unit_register_requests, many=True)

        # Get the list of available courses for the user to choose from
        available_courses = SemesterCourse.objects.exclude(unit_register_request__student=student)
        courses_serializer = SemesterCourseSerializer(available_courses, many=True)

        return Response({"unit_register_requests": serializer.data, "available_courses": courses_serializer.data},
                        status=status.HTTP_200_OK)

    @transaction.atomic()
    def post(self, request, pk):
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

        # Assuming your request data looks like this: {"semester_course": [1, 2, 3]}
        course_ids = request.data.get("semester_course", [])

        if len(course_ids) != len(set(course_ids)):
            return Response({"error": "Duplicate courses are not allowed in a single registration request"},
                            status=status.HTTP_400_BAD_REQUEST)

        # atomic transaction
        with transaction.atomic():
            # Check if the student has passed all prerequisite courses for the selected courses

            for course_id in course_ids:
                course = SemesterCourse.objects.get(pk=course_id)
                prerequisites = course.approved_course.prerequisite.all()
                print(prerequisites)

                if prerequisites:
                    if not student.passed_courses.filter(id__in=prerequisites).exists():
                        error_message = f"Student has not passed all prerequisite courses for course {course_id}"
                        return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)

                existing_courses = student.unit_register_request.values_list('semester_course__id', flat=True)
                if set(course_ids) & set(existing_courses):
                    return Response(
                        {"error": "Duplicate courses are not allowed across multiple registration requests"},
                        status=status.HTTP_400_BAD_REQUEST)

                # Create a new UnitRegisterRequest object for the student
                unit_register_request = UnitRegisterRequest.objects.create(student=student, request_answer="P")

                # Add selected courses to the UnitRegisterRequest
                unit_register_request.semester_course.set(course_ids)

                # Serialize the created object

                serializer = UnitRegisterRequestSerializer(unit_register_request)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


# class CreateRegisterCourse(ListCreateAPIView):
#     # queryset = UnitRegisterRequest.objects.all()
#     serializer_class = UnitRegisterRequestSerializer
#
#     def perform_create(self, serializer):
#         student = self.get_student()
#         serializer.save(student=student)
#
#     def get_student(self):
#         return get_object_or_404(Student, pk=self.kwargs['pk'])
#
#     @transaction.atomic
#     def post(self, request, *args, **kwargs):
#         # Deserialize the request data using the serializer
#         serializer = UnitRegisterRequestSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)  # Ensure the data is valid
#         semester_course_data = serializer.validated_data.get("semester_course")
#
#         course_ids = [course.id for course in semester_course_data]
#
#         print(course_ids)
#
#         return Response({"status": "ok"})


class SubmitRegisterCourse(APIView):
    pass

    # @transaction.atomic
    def post(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        serializer = UnitRegisterRequestSerializer(data=request.data)
        if serializer.is_valid():
            unit_register_request = UnitRegisterRequest(student=student)
            unit_register_request.save()
            # instance
            # serializer.save(instance=unit_register_request)
            print(serializer.data)

            return Response({"status": "ok"})
        return Response(serializer.errors, status=400)
