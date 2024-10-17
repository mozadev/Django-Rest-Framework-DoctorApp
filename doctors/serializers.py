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
            "The email have to include the @example.com"
            )

    def validate(self, attrs):
        if len(attrs["contact_number"]) < 10 and attrs["is_on_vacation"]:
            raise serializers.ValidationError(
                "Please, enter a number before you go on vacations"
            )
        return super().validate(attrs)
    # if not continue with functionality of father class 


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model: Department
        fields = "__all__"


class DoctorAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model: DoctorAvailability
        fields = "__all__"


class MedicalNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model: MedicalNote
        fields = "__all__"
