from django.db import models

DEGREE_CHOICES = (
    ("B", "Bachelor"),
    ("M", "Master"),
    ("P", "PHD"),
)

ACADEMICDEMIC_DEPARTMENT_CHOICES = (
    ("L", "Law"),
    ("S", "Science"),
    ("MS", "Medical Sciences"),
    ("E", "Engineering"),
    ("AA", "Art & Architecture"),
    ("N", "None"),
)

class Department(models.Model):
    name = models.CharField(max_length = 255)

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"

    def __str__(self):
        return self.name

class Major(models.Model):
    name = models.CharField(max_length = 255)
    department = models.ForeignKey(Department, on_delete = models.PROTECT, blank = True, null = True)
    academic_department = models.CharField(max_length = 2, choices = ACADEMICDEMIC_DEPARTMENT_CHOICES, default = "N")
    units_number = models.PositiveIntegerField()
    degree = models.CharField(max_length = 1, choices = DEGREE_CHOICES, default = "B") 

    class Meta:
        verbose_name = "Major"
        verbose_name_plural = "Majors"

    def __str__(self):
        return self.name