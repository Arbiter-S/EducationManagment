from django.contrib import admin
from .models import *


@admin.register(ApprovedCourse)
class ApprovedCourseAdmin(admin.ModelAdmin):
    list_display = ["name", "department", "type", "unit"]
    search_fields = ["name", "department"]
    fieldsets = [
        ("General info", {
            "fields": [
                "name",
                "department",
                "type",
                "unit",
            ],

        }),
        ("Related courses", {
            "fields": [
                "prerequisite",
                "corequisite",
            ]
        })
    ]

    readonly_fields = ("name", "department", "type", "unit")

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = list(super().get_readonly_fields(request, obj))
        if not obj:
            readonly_fields.remove("name")
            readonly_fields.remove("department")
            readonly_fields.remove("type")
            readonly_fields.remove("unit")
        return tuple(readonly_fields)


@admin.register(SemesterCourse)
class SemesterCourseAdmin(admin.ModelAdmin):
    list_display = ["approved_course", "professor", "class_days"]
    search_fields = ["approved_course", "professor", "class_days"]
    readonly_fields = ("approved_course",)

    fieldsets = [
        ("Title", {
            "fields": [
                "approved_course",
            ],
        }),
        ("Class info", {
            "fields": [
                "professor",
                "class_days",
                "class_start_time",
                "class_end_time",
                "capacity",
            ]
        }),
        ("Exam info", {
            "fields": [
                "exam_date",
                "exam_location",
            ]
        })
    ]

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = list(super().get_readonly_fields(request, obj))
        if not obj:
            readonly_fields.remove("approved_course")
        return tuple(readonly_fields)
