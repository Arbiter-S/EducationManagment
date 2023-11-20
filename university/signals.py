from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver

from course_selection.models import *
from course_selection.models import Student

from .models import Term


@receiver(m2m_changed, sender=Term.students.through)
def create_semester(sender, instance, action, **kwargs):
    if action == "post_add":
        students = instance.students.all()
        print(students)

        for student in students:
            if student.get_student_status():
                StudentSemester.objects.create(
                    student=student,
                    previous_semester_average=0,
                    sum_of_unit=0,
                    term_no=instance,
                )
            else:
                previous_average = StudentSemester.objects.get(student=student, term_no=instance).previous_average()
                StudentSemester.objects.create(
                    student=student,
                    previous_semester_averageS=previous_average,
                    sum_of_unit=0,
                    term_no=instance,
                )
