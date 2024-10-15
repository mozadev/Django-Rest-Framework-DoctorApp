from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)


from .models import (
    Doctor,
    Department,
    DoctorAvailability,
    MedicalNote,
)


from .serializers import (
    DoctorSerializer,
    DepartmentSerializer,
    DoctorAvailabilitySerializer,
    MedicalNoteSerializer,
)


class ListDoctorView(ListAPIView, CreateAPIView):
    """
    Get list of scheduled medical appointments
    """

    allowed_method = ["GET", "POST"]
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()


class DetailDoctorsView(RetrieveUpdateDestroyAPIView):
    allowed_method = [
        "GET",
        "PUT",
        "DELETE",
    ]
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()


class ListDepartmentView(ListAPIView, CreateAPIView):
    allowed_method = ["GET", "POST"]
    serializers_class = DepartmentSerializer
    queryset = Department.objects.all()


class DetailDepartmentView(RetrieveUpdateDestroyAPIView):
    allowed_method = ["GET", "PUT", "DELETE"]
    serializer_class = Department
    queryset = Department.objects.all()


class ListDoctorAvailabilityView(ListAPIView, CreateAPIView):
    allowed_method = ["GET", "POST"]
    serializer_class = DoctorAvailabilitySerializer
    queryset = DoctorAvailability.objects.all()


class DetailDoctorAvailabilityView(RetrieveUpdateDestroyAPIView):
    allowed_method = ["GET", "POST", "DELETE"]
    serializer_class = DoctorAvailabilitySerializer
    queryset = DoctorAvailability.objects.all()


class ListMedicalNoteView(ListAPIView, CreateAPIView):
    allowed_method = ["GET", "POST"]
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()


class DetailMedicalNoteView(RetrieveUpdateDestroyAPIView):
    allowed_method = ["GET", "POST"]
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()

    
