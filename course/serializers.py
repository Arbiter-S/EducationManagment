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
