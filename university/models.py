from django.db import models

from course.models import ApprovedCourse
from user.models import Professor, Student


class Term(models.Model):
    semester_code = models.IntegerField(unique=True, primary_key=True)
    students = models.ManyToManyField(Student)
    lecturers = models.ManyToManyField(Professor)
    course = models.ManyToManyField(ApprovedCourse)
    start_date_unit_selection = models.DateTimeField()
    end_date_unit_selection = models.DateTimeField()
    start_date_class = models.DateTimeField()
    end_date_class = models.DateTimeField()
    start_date_rechoice = models.DateTimeField()
    end_date_rechoice = models.DateTimeField()
    start_date_of_w = models.DateField()
    end_date_of_w = models.DateField()
    start_date_of_delete_semester = models.DateField()
    end_date_of_delete_semester = models.DateField()
    start_date_of_exams = models.DateField()
    end_date_of_exams = models.DateField()

    def __str__(self):
        return f'Term {self.semester_code}'
