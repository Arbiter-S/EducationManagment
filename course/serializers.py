from rest_framework import serializers
from .models import ApprovedCourse, SemesterCourse


class ApprovedCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApprovedCourse
        fields = ['name', 'department', 'type', 'unit', 'prerequisite', 'corequisite']


class SemesterCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SemesterCourse
        fields = "__all__"
