from rest_framework import serializers
from .models import ApprovedCourse

class ApprovedCoueseSerializer(serializers.ModelSerializer):

    class Meta:
        model = ApprovedCourse
        fields = ['name', 'department', 'type', 'unit', 'prerequisite', 'corequisite']
