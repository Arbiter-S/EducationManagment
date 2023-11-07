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


class IsITAdminOrIsEducationalAssistant(BasePermission):
    message = "Permission Denied. You don't have any access!"

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            user_role = request.user.role
            if user_role == 'ADM':
                return True

            if user_role == 'AST':
                assistant = EducationalAssistant.objects.get(pk=request.user.pk)
                print(assistant)
                department = assistant.department
                print(department)
                if department == request.data.get('department'):
                    print(request.data.get('department'))
                    return True



        return False


# {
#     "name": "",
#     "department": "",
#     "exam_date": null,
#     "exam_location": "",
#     "class_days": null,
#     "class_end_time": null,
#     "class_start_time": null,
#     "capacity": null,
#     "approved_course": null,
#     "professor": null
# }
#enginer edutional assitant
#AST-3055039170

# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk5MjkxNDA1LCJpYXQiOjE2OTkyOTA1MDUsImp0aSI6IjQ3NTNjMDZlNzUwMDQ2ZGM4YmJiMmMwNDA0NzAwZDBiIiwidXNlcl9pZCI6Ijk2OTk2YjE1LTlmOTYtNDhjMS1iNDE3LTk2YzdlMzM4ODFjZiJ9.zOSlnyKQNS5cYKkWNAgMxi7R_OHWPpt6d0yp_nhbSNE

#art assistant
# AST-5913821171

# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk5MjkxODEwLCJpYXQiOjE2OTkyOTA5MTAsImp0aSI6IjljZTFjNjQ3ZjQyNDRhM2NhOTg1OTZkYmRmNWRmMjlhIiwidXNlcl9pZCI6IjU2YmE4MDc3LWE4MWEtNDA2NC1hMTNmLWFiZWM1ODY1Y2Y3OSJ9.4ATmVQtR__8qsuyVMeUTqZo6nTTGDL2dnE-sLSJMPek