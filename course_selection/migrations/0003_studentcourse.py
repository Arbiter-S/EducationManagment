# Generated by Django 4.2.7 on 2023-11-07 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_rename_academic_years_student_academic_terms'),
        ('course', '0002_initial'),
        ('course_selection', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('pass_or_fail', models.CharField(choices=[('P', 'Pass'), ('F', 'Failed')], max_length=1)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='course.approvedcourse')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.student')),
            ],
        ),
    ]
