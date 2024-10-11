from rest_framework import serializers

from .models import Doctor, Department, DoctorAvailability, MedicalNote


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"

    def validate_email(self, value):
        if "@example.com" in value:
            return value
        raise serializers.ValidationError(
            "The email should be include @example"
        )

    def validate(self, attrs):
        if len(attrs["contact_number"]) < 10 and attrs["is_on_vacation"]:
            raise serializers.ValidationError(
                "Please, Enter a valid number before you go on vacations"
            )
        return super().validate(attrs)
