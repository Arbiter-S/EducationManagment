# Generated by Django 4.2.6 on 2023-10-29 14:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import user.validators
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("department", "0001_initial"),
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "user_code",
                    models.CharField(blank=True, max_length=14, null=True, unique=True),
                ),
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254, unique=True)),
                (
                    "national_code",
                    models.CharField(
                        max_length=10,
                        unique=True,
                        validators=[user.validators.national_code],
                    ),
                ),
                (
                    "phone_number",
                    models.CharField(
                        max_length=11,
                        unique=True,
                        validators=[user.validators.phone_number],
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female")], max_length=1
                    ),
                ),
                (
                    "birth_date",
                    models.DateField(validators=[user.validators.birth_date]),
                ),
                (
                    "role",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("STU", "Student"),
                            ("PRO", "Professor"),
                            ("AST", "Assistant"),
                            ("ADM", "Admin"),
                        ],
                        max_length=3,
                        null=True,
                    ),
                ),
                ("is_staff", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "User",
                "verbose_name_plural": "Users",
            },
        ),
        migrations.CreateModel(
            name="ITAdmin",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "IT Admin",
                "verbose_name_plural": "IT Admins",
            },
        ),
        migrations.CreateModel(
            name="Professor",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("expertise", models.CharField(max_length=255)),
                (
                    "position",
                    models.CharField(
                        choices=[
                            ("P", "Professor"),
                            ("S", "Supervisor"),
                            ("L", "Lecturer"),
                        ],
                        default="P",
                        max_length=1,
                    ),
                ),
                (
                    "department",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="department.department",
                    ),
                ),
                (
                    "major",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="department.major",
                    ),
                ),
            ],
            options={
                "verbose_name": "Professor",
                "verbose_name_plural": "Professors",
            },
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "degree",
                    models.CharField(
                        choices=[("B", "Bachelor"), ("M", "Master"), ("D", "Doctoral")],
                        default="B",
                        max_length=1,
                    ),
                ),
                ("entry_year", models.CharField(max_length=4)),
                ("entry_semester", models.CharField(max_length=255)),
                (
                    "average",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=4, null=True
                    ),
                ),
                ("is_not_soldier", models.BooleanField(default=True)),
                (
                    "military_status",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "department",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="department.department",
                    ),
                ),
                (
                    "major",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="department.major",
                    ),
                ),
                (
                    "supervisor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="user.professor"
                    ),
                ),
            ],
            options={
                "verbose_name": "Student",
                "verbose_name_plural": "Students",
            },
        ),
        migrations.CreateModel(
            name="EducationalAssistant",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "department",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="department.department",
                    ),
                ),
                (
                    "major",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="department.major",
                    ),
                ),
            ],
            options={
                "verbose_name": "Educational Assistant",
                "verbose_name_plural": "Educational Assistants",
            },
        ),
    ]