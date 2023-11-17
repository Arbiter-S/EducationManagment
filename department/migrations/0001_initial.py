# Generated by Django 4.2.6 on 2023-11-15 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Department',
                'verbose_name_plural': 'Departments',
            },
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('academic_department', models.CharField(choices=[('L', 'Law'), ('S', 'Science'), ('MS', 'Medical Sciences'), ('E', 'Engineering'), ('AA', 'Art & Architecture'), ('N', 'None')], default='N', max_length=2)),
                ('units_number', models.PositiveIntegerField()),
                ('degree', models.CharField(choices=[('B', 'Bachelor'), ('M', 'Master'), ('P', 'PHD')], default='B', max_length=1)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='department.department')),
            ],
            options={
                'verbose_name': 'Major',
                'verbose_name_plural': 'Majors',
            },
        ),
    ]
