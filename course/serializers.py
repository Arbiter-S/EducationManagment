from rest_framework import serializers
from .models import *


class ApprovedCoueseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApprovedCourse
        fields = ['name', 'department', 'type', 'unit', 'prerequisite', 'corequisite']


class SemesterCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SemesterCourse
        field = '__all__'

    # def validate(self, attrs):
    #     # check for date

