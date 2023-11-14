from rest_framework import serializers

from .models import UnitRegisterRequest


class UnitRegisterRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitRegisterRequest
        fields = ["student", "semester_course"]
        extra_kwargs = {"request_answer": {"read_only": True}}
