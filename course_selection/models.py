from django.db import models

from course.models import *
from user.models import *

CHOICES_BOOLEANO_SIM_NAO = (
    ("A", 'accepted'),
    ("D", 'decline'),
    ("P", 'pending'),
)
STATUS_CHOICES = (
    ("P", "Pass"),
    ("F", "Failed"),
)


class UnitRegisterRequest(models.Model):
    student = models.ForeignKey(Student, on_delete=models.PROTECT, related_name='unit_register_request')
    semester_course = models.ManyToManyField(SemesterCourse, related_name='unit_register_request')
    request_answer = models.CharField(max_length=1, choices=CHOICES_BOOLEANO_SIM_NAO, default="P")

    def __str__(self):
        return f'{self.student.user.first_name} {self.student.user.last_name} ({self.student.user.username})'


class StudentCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    course = models.ForeignKey(ApprovedCourse, on_delete=models.DO_NOTHING)
    score = models.IntegerField()
    pass_or_fail = models.CharField(max_length=1, choices=STATUS_CHOICES)
