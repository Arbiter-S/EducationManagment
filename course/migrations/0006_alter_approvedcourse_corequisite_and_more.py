# Generated by Django 4.2.6 on 2023-11-01 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_alter_approvedcourse_corequisite_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approvedcourse',
            name='corequisite',
            field=models.ManyToManyField(blank=True, to='course.approvedcourse'),
        ),
        migrations.AlterField(
            model_name='approvedcourse',
            name='prerequisite',
            field=models.ManyToManyField(blank=True, to='course.approvedcourse'),
        ),
    ]