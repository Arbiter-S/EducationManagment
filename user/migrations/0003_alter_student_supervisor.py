# Generated by Django 4.2.7 on 2023-11-09 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_student_passed_courses_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='supervisor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.professor'),
        ),
    ]