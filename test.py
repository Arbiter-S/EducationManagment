from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

from university.models import *

from .validators import *

import uuid

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

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password = None, **extra_fields):
        if not email:
            raise ValueError("The Email Field Must Be Set")
        email = self.normalize_email(email)
        user.set_password(password)
        user = self.model(email = email, **extra_fields)
        user.save()
        return user

    def create_superuser(self, email, password = None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser Must Have is_staff = True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser Must Have is_superuser = True")
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key = True, unique = True, default = uuid.uuid4, editable = False)
    user_code = models.CharField(max_length = 14, unique = True, blank = True, null = True)
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.EmailField(unique = True)
    national_code = models.CharField(max_length = 10, unique = True, validators = [national_code])
    phone_number = models.CharField(max_length = 11, unique = True, validators = [phone_number])
    gender = models.CharField(max_length = 1, choices = GENDER_CHOICES)
    birth_date = models.DateField(validators = [birth_date])
    # Profile Picture
    role = models.CharField(max_length = 3, choices = ROLE_CHOICES, blank = True, null = True)
    is_staff = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "national_code", "phone_number", "gender", "birth_date", "role"]

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.user_code})"

class Student(models.Model):
    user = models.OneToOneField("User", on_delete = models.DO_NOTHING, primary_key = True)
    department = models.ForeignKey(Department, on_delete = models.PROTECT)
    major = models.ForeignKey(Major, on_delete = models.PROTECT)
    degree = models.CharField(max_length = 1, choices = DEGREE_CHOICES, default = "B") 
    entry_year = models.CharField(max_length = 4)
    entry_semester = models.CharField(max_length = 255)
    # passed_courses = ...
    # passing_courses = ...
    average = models.DecimalField(max_digits = 4, decimal_places = 2, blank = True, null = True)
    is_not_soldier = models.BooleanField(default = True)
    military_status = models.CharField(max_length = 255, blank = True, null = True)
    supervisor = models.ForeignKey("Professor", on_delete = models.PROTECT)
    # academic_years = ...

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def get_military_status(self):
        if self.is_not_soldier:
            return "Not Soldier"
        else:
            return "Soldier"

    def clean(self):
        super().clean()
        if Professor.objects.filter(user = self.user).exists() or EducationalAssistant.objects.filter(user = self.user).exists() or ITAdmin.objects.filter(user = self.user).exists():
            raise ValidationError("This User Is Already Assigned To a Different Role")

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class Professor(models.Model):
    user = models.OneToOneField("User", on_delete = models.DO_NOTHING, primary_key = True)
    department = models.ForeignKey(Department, on_delete = models.PROTECT)
    major = models.ForeignKey(Major, on_delete = models.PROTECT)
    expertise = models.CharField(max_length = 255)
    position = models.CharField(max_length = 1, choices = POSITION_CHOICES, default = "P") 
    # past_teaching_courses = ...

    class Meta:
        verbose_name = "Professor"
        verbose_name_plural = "Professors"

    def clean(self):
        super().clean()
        if Student.objects.filter(user = self.user).exists() or EducationalAssistant.objects.filter(user = self.user).exists() or ITAdmin.objects.filter(user = self.user).exists():
            raise ValidationError("This User Is Already Assigned To a Different Role")

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class EducationalAssistant(models.Model):
    user = models.OneToOneField("User", on_delete = models.DO_NOTHING, primary_key = True)
    department = models.ForeignKey(Department, on_delete = models.PROTECT)
    major = models.ForeignKey(Major, on_delete = models.PROTECT)

    class Meta:
        verbose_name = "Educational Assistant"
        verbose_name_plural = "Educational Assistants"

    def clean(self):
        super().clean()
        if Student.objects.filter(user = self.user).exists() or Professor.objects.filter(user = self.user).exists() or ITAdmin.objects.filter(user = self.user).exists():
            raise ValidationError("This User Is Already Assigned To a Different Role")

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class ITAdmin(models.Model):
    user = models.OneToOneField("User", on_delete = models.DO_NOTHING, primary_key = True)

    class Meta:
        verbose_name = "IT Admin"
        verbose_name_plural = "IT Admins"

    def clean(self):
        super().clean()
        if Student.objects.filter(user = self.user).exists() or Professor.objects.filter(user = self.user).exists() or EducationalAssistant.objects.filter(user = self.user).exists():
            raise ValidationError("This User Is Already Assigned To a Different Role")

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"