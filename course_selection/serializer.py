from rest_framework import serializers
from .models import UnitRegisterRequest


class UnitRegisterRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitRegisterRequest
        fields = ["semester_course", "request_answer"]
        extra_kwargs = {"request_answer": {"read_only": True}}
