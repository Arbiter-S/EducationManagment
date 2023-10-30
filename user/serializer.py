from rest_framework.serializers import ModelSerializer

from .models import  *

class ProfessorSerializer(ModelSerializer):
    class Meta:
        model = Professor
        fields = "__all__"

class EducationalAssistantSerializer(ModelSerializer):
    class Meta:
        model = EducationalAssistant
        fields = "__all__"