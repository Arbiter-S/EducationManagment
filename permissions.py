from rest_framework.permissions import BasePermission

from university.models import *
from user.models import EducationalAssistant, ITAdmin, Student


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


class IsStudentRegisterInCurrentTerm(BasePermission):
    message = "You did not register in this term"

    def has_permission(self, request, view):
        student_pk = request.parser_context['kwargs']['pk']
        student = Student.objects.get(pk=student_pk)
        term_id = request.parser_context['kwargs']['semester_code']

        is_registered = Term.objects.filter(pk=term_id, students=student).exists()

        return is_registered


class IsITAdminOrIsStudent(BasePermission):
    message = "Permission Denied, You don't have any access!"

    def has_permission(self, request, view):
        student_pk = request.parser_context['kwargs']['pk']
        user = request.user.pk == student_pk or request.user.role == "ADM"
        return user


class IsITAdminOrIsEducationalAssistant(BasePermission):
    message = "Permission Denied. You don't have any access!"

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            user_role = request.user.role
            if user_role == 'ADM':
                return True

            if user_role == 'AST':
                assistant = EducationalAssistant.objects.get(pk=request.user.pk)
                department = assistant.department
                if department == request.data.get('department'):
                    return True

        return False


class IsAssistant(BasePermission):
    message = "Permission Denied. You are not an assistant!"

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            user_role = request.user.role

            if user_role == 'AST':
                return True

        return False


class IsOwner(BasePermission):
    message = "Permission Denied. You are not the owner!"

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            current_user_pk = str(request.user.pk)
            requested_profile_pk = str(view.kwargs.get('pk'))
            if requested_profile_pk == current_user_pk:
                return True

            if request.data.get('pk') == current_user_pk:
                return True

        else:
            return False
