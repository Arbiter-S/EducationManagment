import django_filters
from rest_framework import serializers
from .models import *


class ApprovedCoueseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApprovedCourse
        fields = ['name', 'department', 'type', 'unit', 'prerequisite', 'corequisite']


class SemesterCourseSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='approved_course.name', allow_blank=True)
    department = serializers.CharField(source='approved_course.department', allow_blank=True)

    # Will add term after term model
    class Meta:
        model = SemesterCourse
        fields = '__all__'

    # def validate(self, attrs):
    #     # check for date


class SemesterCourseFilterSet(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='approved_course__name')
    department = django_filters.CharFilter(field_name='approved_course__department')
    # Will add term after term model


class StudentCourseReadSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='approved_course.name')
    professor_name = serializers.SerializerMethodField()

    def get_professor_name(self, obj):
        first_name = obj.professor.user.first_name
        last_name = obj.professor.user.last_name

        return f'{first_name} {last_name}'

    class Meta:
        model = SemesterCourse
        fields = ['name', 'professor_name', 'class_days', 'class_start_time', 'class_end_time']


class ExamsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='approved_course.name')

    class Meta:
        model = SemesterCourse
        fields = ['name', 'exam_date', 'exam_location']
