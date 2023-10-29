from rest_framework import serializers
from . import  models

class EducationalAssistantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EducationalAssistant
        fields = '__all__'