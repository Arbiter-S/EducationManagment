from rest_framework import serializers
from .models import UnitRegisterRequest


class UnitRegisterRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitRegisterRequest
        fields = "__all__"
        extra_kwargs = {"request_answer": {"read_only": True}}


