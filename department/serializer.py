from rest_framework.serializers import ModelSerializer

from .models import *


class FacultySerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"