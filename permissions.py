from rest_framework.permissions import BasePermission

from user.models import ITAdmin, Student, EducationalAssistant


class IsITAdmin(BasePermission):
    message = "Permission Denied. You're Not an IT Admin"

    def has_permission(self, request, view):
        user = request.user.is_authenticated and request.user.role == "ADM"
        is_itadmin = ITAdmin.objects.filter(user=request.user).exists()
        return user and is_itadmin


class IsITAdminOrIsEducationalAssistantOrIsSupervisor(BasePermission):
    message = "Permission Denied. You don't have any access!"

    def has_permission(self, request, view):
        student_pk = request.parser_context['kwargs']['pk']
        student = Student.objects.get(pk=student_pk)
        student_supervisor = student.supervisor
        student_department = student.department
        user = request.user.is_authenticated and request.user.role == "ADM" or request.user.pk == student_supervisor.pk \
               or request.user.educationalassistant.department.name == student_department.name
        return user


class IsITAdminOrIsStudent(BasePermission):
    message = "Permission Denied, You don't have any access!"

    def has_permission(self, request, view):
        student_pk = request.parser_context['kwargs']['pk']
        user = request.user.pk == student_pk or request.user.role == "ADM"
        return user
