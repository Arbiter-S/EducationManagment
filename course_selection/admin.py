from django.contrib import admin

from .models import *


@admin.register(UnitRegisterRequest)
class UnitRegisterRequest(admin.ModelAdmin):
    pass

@admin.register(StudentCourse)
class StudentCourseAdmin(admin.ModelAdmin):
    pass
