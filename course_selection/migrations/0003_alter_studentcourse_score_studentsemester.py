# Generated by Django 4.2.7 on 2023-11-15 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_alter_semestercourse_professor'),
        ('university', '0002_initial'),
        ('user', '0003_alter_student_supervisor'),
        ('course_selection', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentcourse',
            name='score',
            field=models.FloatField(),
        ),
        migrations.CreateModel(
            name='StudentSemester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester_average', models.FloatField()),
                ('sum_of_unit', models.IntegerField()),
                ('courses', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='course.semestercourse')),
                ('semester_no', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='university.term')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='student_semester', to='user.student')),
            ],
        ),
    ]