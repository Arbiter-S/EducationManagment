# Generated by Django 4.2.7 on 2023-11-15 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_selection', '0007_alter_studentsemester_courses'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentsemester',
            old_name='semester_average',
            new_name='previous_semester_average',
        ),
    ]
