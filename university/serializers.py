from rest_framework import serializers
from .models import *


class TermSerializer(serializers.ModelSerializer):
    class Meta:
        model = Term
        fields = '__all__'

