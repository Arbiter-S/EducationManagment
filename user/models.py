from django.contrib.auth.models import AbstractUser
from course.models import *

import uuid

from department.models import *

from .validators import *

GENDER_CHOICES = (
    ("M", "Male"),
    ("F", "Female"),
)

ROLE_CHOICES = (
    ("STU", "Student"),
    ("PRO", "Professor"),
    ("AST", "Assistant"),
    ("ADM", "Admin"),
)

DEGREE_CHOICES = (
    ("B", "Bachelor"),
    ("M", "Master"),
    ("D", "Doctoral"),
)

POSITION_CHOICES = (
    ("P", "Professor"),
    ("S", "Supervisor"),
    ("L", "Lecturer"),
)


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=14, unique=True, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    national_code = models.CharField(max_length=10, blank=True, null=True, validators=[national_code])
    phone_number = models.CharField(max_length=11, unique=True, blank=True, null=True, validators=[phone_number])
    gender = models.CharField(max_length=1, blank=True, null=True, choices=GENDER_CHOICES)
    birth_date = models.DateField(blank=True, null=True, validators=[birth_date])
    # Profile Picture
    role = models.CharField(max_length=3, choices=ROLE_CHOICES, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"


class Student(models.Model):
    user = models.OneToOneField("User", on_delete=models.DO_NOTHING, primary_key=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    major = models.ForeignKey(Major, on_delete=models.PROTECT)
    degree = models.CharField(max_length=1, choices=DEGREE_CHOICES, default="B")
    entry_year = models.CharField(max_length=4)
    entry_semester = models.CharField(max_length=255)
    passed_courses = models.ManyToManyField(ApprovedCourse, related_name="student_passed_course")
    passing_courses = models.ManyToManyField(SemesterCourse, related_name="student_passing_course")
    average = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    is_soldier = models.BooleanField(default=False)
    military_status = models.CharField(max_length=255, blank=True, null=True)
    supervisor = models.ForeignKey("Professor", on_delete=models.PROTECT)
    academic_terms = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def get_military_status(self):
        if self.is_soldier:
            return "Soldier"
        else:
            return "Not Soldier"

    def clean(self):
        super().clean()
        if Professor.objects.filter(user=self.user).exists() or EducationalAssistant.objects.filter(
                user=self.user).exists() or ITAdmin.objects.filter(user=self.user).exists():
            raise ValidationError("This User Is Already Assigned To a Different Role")

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Professor(models.Model):
    user = models.OneToOneField("User", on_delete=models.DO_NOTHING, primary_key=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    major = models.ForeignKey(Major, on_delete=models.PROTECT)
    expertise = models.CharField(max_length=255)
    position = models.CharField(max_length=1, choices=POSITION_CHOICES, default="P")

    # Past Teaching Courses 

    class Meta:
        verbose_name = "Professor"
        verbose_name_plural = "Professors"

    def clean(self):
        super().clean()
        if Student.objects.filter(user=self.user).exists() or EducationalAssistant.objects.filter(
                user=self.user).exists() or ITAdmin.objects.filter(user=self.user).exists():
            raise ValidationError("This User Is Already Assigned To a Different Role")

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class EducationalAssistant(models.Model):
    user = models.OneToOneField("User", on_delete=models.DO_NOTHING, primary_key=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    major = models.ForeignKey(Major, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Educational Assistant"
        verbose_name_plural = "Educational Assistants"

    def clean(self):
        super().clean()
        if Student.objects.filter(user=self.user).exists() or Professor.objects.filter(
                user=self.user).exists() or ITAdmin.objects.filter(user=self.user).exists():
            raise ValidationError("This User Is Already Assigned To a Different Role")

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class ITAdmin(models.Model):
    user = models.OneToOneField("User", on_delete=models.DO_NOTHING, primary_key=True)

    class Meta:
        verbose_name = "IT Admin"
        verbose_name_plural = "IT Admins"

    def clean(self):
        super().clean()
        if Student.objects.filter(user=self.user).exists() or Professor.objects.filter(
                user=self.user).exists() or EducationalAssistant.objects.filter(user=self.user).exists():
            raise ValidationError("This User Is Already Assigned To a Different Role")

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
