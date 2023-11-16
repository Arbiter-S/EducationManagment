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
from .models import *
from university.models import *


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
    permission_classes = [IsStudentRegisterInCurrentTerm]

    def get(self, request, pk, semester_code):
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

        semester_code = Term.objects.get(semester_code=semester_code)

        # Get the UnitRegisterRequest objects for the specific student
        unit_register_requests = UnitRegisterRequest.objects.filter(student=student, semester_code=semester_code)

        # Serialize the data
        serializer = UnitRegisterRequestSerializer(unit_register_requests, many=True)

        # Get the list of available courses for the user to choose from
        available_courses = SemesterCourse.objects.exclude(unit_register_request__student=student)
        courses_serializer = SemesterCourseSerializer(available_courses, many=True)

        return Response({"unit_register_requests": serializer.data, "available_courses": courses_serializer.data},
                        status=status.HTTP_200_OK)

    @transaction.atomic()
    def post(self, request, pk, semester_code):
        try:
            student = Student.objects.get(pk=pk)

        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
        semester = Term.objects.get(semester_code=semester_code)

        # Assuming your request data looks like this: {"courses": [1, 2, 3]}
        course_ids = request.data.get("courses", [])

        if len(course_ids) != len(set(course_ids)):
            return Response({"error": "Duplicate courses are not allowed in a single registration request"},
                            status=status.HTTP_400_BAD_REQUEST)

        # atomic transaction
        with transaction.atomic():
            # Check if the student has passed all prerequisite courses for the selected courses

            for course_id in course_ids:
                course = SemesterCourse.objects.get(pk=course_id)
                prerequisites = course.approved_course.prerequisite.all()

                if prerequisites:
                    if not student.passed_courses.filter(id__in=prerequisites).exists():
                        error_message = f"Student has not passed all prerequisite courses for course {course_id}"
                        return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)

                existing_courses = student.unit_register_request.values_list('semester_course__id', flat=True)
                if set(course_ids) & set(existing_courses):
                    return Response(
                        {"error": "Duplicate courses are not allowed across multiple registration requests"},
                        status=status.HTTP_400_BAD_REQUEST)

                if course.capacity == 0:
                    print("True")
                    return Response(
                        {"error": "This course doesn't have capacity:) "},
                        status=status.HTTP_400_BAD_REQUEST)
                course.capacity -= 1
                course.save()

                # Check student's average for checking limit of units
                previous_term = Term.objects.exclude(semester_code=semester_code).last()

                if previous_term is None:
                    student_average = 0
                else:
                    student_average = StudentSemester.objects.get(student=student,
                                                                  term_no=previous_term).previous_average()

                student_semester = StudentSemester.objects.get(student=student)
                if student_average < 17 < student_semester.sum_of_unit:
                    return Response(
                        {"error": "Your average is less than 17 and you can not select more than 17 units!"},
                        status=status.HTTP_400_BAD_REQUEST)
                else:
                    if student_semester.sum_of_unit > 24:
                        return Response(
                            {"error": "You can not select more than 24 units!"}
                        )

                # Create a new UnitRegisterRequest object for the student
                unit_register_request = UnitRegisterRequest.objects.create(student=student, semester_code=semester,
                                                                           request_answer="P")
                # unit_count = StudentSemester.objects.get(student=student).sum_of_unit
                student_semester.sum_of_unit += course.approved_course.unit
                student_semester.save()

                # Add selected courses to the UnitRegisterRequest
                unit_register_request.semester_course.set(course_ids)

                # Serialize the created object

                serializer = UnitRegisterRequestSerializer(unit_register_request)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
