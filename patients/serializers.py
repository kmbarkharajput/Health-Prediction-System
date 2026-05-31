from rest_framework import serializers
from .models import Patient


class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = '__all__'

    def validate_glucose(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "Glucose cannot be negative."
            )
        return value

    def validate_haemoglobin(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "Haemoglobin cannot be negative."
            )
        return value

    def validate_cholesterol(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "Cholesterol cannot be negative."
            )
        return value    