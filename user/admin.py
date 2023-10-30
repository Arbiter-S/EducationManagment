from django.contrib import admin

from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "user_code", "national_code", "email", "phone_number", "gender", "birth_date", "id")
    search_fields = ("id", "first_name", "last_name", "user_code", "national_code", "email", "phone_number", "gender", "birth_date")
    list_per_page = 20

    fieldsets = (
        ("Personal Information", {
            "fields": ("id", "first_name", "last_name", "user_code", "national_code", "email", "phone_number", "password", "gender", "birth_date", "role"),
        }),
        ("Permissions", {
            "fields": ("is_staff", "is_superuser", "groups", "user_permissions"),
        }),
        ("Important dates", {
            "fields": ("last_login", ),
        }),
    )

    readonly_fields = ("id", "first_name", "last_name", "user_code", "national_code", "password", "gender", "birth_date", "is_staff", "is_superuser", "last_login", "role")

    def get_readonly_fields(self, request, obj = None):
        readonly_fields = ["id", "user_code", "last_login", "is_staff", "is_superuser"]
        if obj:
            readonly_fields.extend(self.readonly_fields)
        return readonly_fields

class StudentAdmin(admin.ModelAdmin):
    list_display = ("user_first_name", "user_last_name", "get_user_code", "department", "major", "degree", "entry_year", "entry_semester", "get_military_status", "supervisor")
    search_fields = ("user__first_name", "user__last_name", "user__national_code")
    list_per_page = 20

    fieldsets = (
        ("Student Information", {
            "fields": (
                "user",
                "department",
                "major",
                "degree",
                "entry_year",
                "entry_semester",
                "average",
                "is_not_soldier",
                "military_status",
                "supervisor",
            ),
        }),
    )

    def user_first_name(self, obj):
        return obj.user.first_name

    user_first_name.short_description = "First Name"

    def user_last_name(self, obj):
        return obj.user.last_name

    user_last_name.short_description = "Last Name"

    def get_user_code(self, obj):
        return obj.user.user_code

    get_user_code.short_description = "User Code"

class ProfessorAdmin(admin.ModelAdmin):
    list_display = ("user_first_name", "user_last_name", "get_user_code", "department", "major", "expertise", "position")
    search_fields = ("user__first_name", "user__last_name", "user__national_code")
    list_per_page = 20

    fieldsets = (
        ("Professor Information", {
            "fields": (
                "user",
                "department",
                "major",
                "expertise",
                "position",
            ),
        }),
    )

    def user_first_name(self, obj):
        return obj.user.first_name

    user_first_name.short_description = "First Name"

    def user_last_name(self, obj):
        return obj.user.last_name

    user_last_name.short_description = "Last Name"

    def get_user_code(self, obj):
        return obj.user.user_code

    get_user_code.short_description = "User Code"

class EducationalAssistantAdmin(admin.ModelAdmin):
    list_display = ("user_first_name", "user_last_name", "get_user_code", "department", "major")
    search_fields = ("user__first_name", "user__last_name", "user__national_code")
    list_per_page = 20

    fieldsets = (
        ("Educational Assistant Information", {
            "fields": (
                "user",
                "department",
                "major",
            ),
        }),
    )

    def user_first_name(self, obj):
        return obj.user.first_name

    user_first_name.short_description = "First Name"

    def user_last_name(self, obj):
        return obj.user.last_name

    user_last_name.short_description = "Last Name"

    def get_user_code(self, obj):
        return obj.user.user_code

    get_user_code.short_description = "User Code"

class ITAdminAdmin(admin.ModelAdmin):
    list_display = ("user_first_name", "user_last_name", "get_user_code")
    search_fields = ("user__first_name", "user__last_name", "user__national_code")
    list_per_page = 20

    fieldsets = (
        ("IT Admin Information", {
            "fields": (
                "user",
            ),
        }),
    )

    def user_first_name(self, obj):
        return obj.user.first_name

    user_first_name.short_description = "First Name"

    def user_last_name(self, obj):
        return obj.user.last_name

    user_last_name.short_description = "Last Name"

    def get_user_code(self, obj):
        return obj.user.user_code

    get_user_code.short_description = "User Code"

admin.site.register(User, UserAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(EducationalAssistant, EducationalAssistantAdmin)
admin.site.register(ITAdmin, ITAdminAdmin)