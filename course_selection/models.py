from django.db import models

from course.models import *
from user.models import *
from university.models import Term

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
    semester_code = models.ForeignKey(Term, on_delete=models.DO_NOTHING)
    request_answer = models.CharField(max_length=1, choices=CHOICES_BOOLEANO_SIM_NAO, default="P")

    def __str__(self):
        return f'{self.student.user.first_name} {self.student.user.last_name} ({self.student.user.username})'


class StudentCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    course = models.ForeignKey(ApprovedCourse, on_delete=models.DO_NOTHING)
    score = models.FloatField()
    pass_or_fail = models.CharField(max_length=1, choices=STATUS_CHOICES)


class StudentSemester(models.Model):
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING, related_name="student_semester")
    previous_semester_average = models.FloatField()
    sum_of_unit = models.IntegerField(null=True)
    courses = models.ManyToManyField(SemesterCourse, blank=True)
    term_no = models.ForeignKey(Term, on_delete=models.DO_NOTHING)

    def previous_average(self):
        try:
            previous_term = Term.objects.exclude(semester_code=self.term_no.semester_code).last()

        except:
            previous_term = Term.objects.get(semester_code=self.term_no.semester_code)

        concat_semester = int(str(self.student.entry_year) + str(self.student.entry_semester))

        if self.term_no.semester_code != concat_semester:
            student_average = StudentSemester.objects.get(student=self.student,
                                                          term_no=previous_term).previous_semester_average
        else:
            student_average = 0

        return student_average
