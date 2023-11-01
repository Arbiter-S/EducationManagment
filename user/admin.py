from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import *

from . signals import *

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(required = False, widget = forms.TextInput())

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ("username",)

class CustomUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = CustomUserCreationForm
    list_display = ("username", "first_name", "last_name", "national_code", "email", "phone_number", "gender", "birth_date", "role")
    search_fields = ("username", "first_name", "last_name", "national_code", "email", "phone_number", "gender", "birth_date", "role")
    list_filter = ()
    list_per_page = 10

    fieldsets = (
        ("Personal info", {"fields": ("id", "first_name", "last_name", "national_code", "email", "phone_number", "gender", "birth_date", "role")}),
        ("Authentication", {"fields": ("username", "password")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
    )

    add_fieldsets = (
        ("Personal info", {"fields": ("first_name", "last_name", "email", "national_code", "phone_number", "gender", "birth_date", "role")}),
        ("Authentication", {
            "classes": ("wide",),
            "fields": ("username", "password1", "password2"),
        }),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
    )

    readonly_fields = ("id", "username", "first_name", "last_name", "national_code", "gender", "birth_date", "role", "password", "is_active", "is_staff", "is_superuser", "last_login", "date_joined")
    
    def get_readonly_fields(self, request, obj = None):
        readonly_fields = list(super().get_readonly_fields(request, obj))
        if not obj:
            readonly_fields.remove("first_name")
            readonly_fields.remove("last_name")
            readonly_fields.remove("national_code")
            readonly_fields.remove("gender")
            readonly_fields.remove("birth_date")
            readonly_fields.remove("role")
        return tuple(readonly_fields)

class StudentAdmin(admin.ModelAdmin):
    list_display = ("user_username", "user_first_name", "user_last_name", "department", "major", "degree", "entry_year", "entry_semester", "get_military_status", "supervisor")
    search_fields = ("user__first_name", "user__last_name", "user__national_code")
    list_filter = ()
    list_per_page = 10

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
                "is_soldier",
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

    def user_username(self, obj):
        return obj.user.username

    user_username.short_description = "Username"

class ProfessorAdmin(admin.ModelAdmin):
    list_display = ("user_username", "user_first_name", "user_last_name", "department", "major", "expertise", "position")
    search_fields = ("user__first_name", "user__last_name", "user__national_code")
    list_filter = ()
    list_per_page = 10

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

    def user_username(self, obj):
        return obj.user.username

    user_username.short_description = "Username"

class EducationalAssistantAdmin(admin.ModelAdmin):
    list_display = ("user_username", "user_first_name", "user_last_name", "department", "major")
    search_fields = ("user__first_name", "user__last_name", "user__national_code")
    list_filter = ()
    list_per_page = 10

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

    def user_username(self, obj):
        return obj.user.username

    user_username.short_description = "Username"

class ITAdminAdmin(admin.ModelAdmin):
    list_display = ("user_username", "user_first_name", "user_last_name")
    search_fields = ("user__first_name", "user__last_name", "user__national_code")
    list_filter = ()
    list_per_page = 10

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

    def user_username(self, obj):
        return obj.user.username

    user_username.short_description = "Username"

admin.site.register(User, CustomUserAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(EducationalAssistant, EducationalAssistantAdmin)
admin.site.register(ITAdmin, ITAdminAdmin)