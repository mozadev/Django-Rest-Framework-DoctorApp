from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .models import Appointment, MedicalNote
from .serializers import AppointmentSerializer, MedicalNoteSerializer


class ListAppointmentView(ListAPIView, CreateAPIView):
    allowed_method = ["GET", "POST"]
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()


class DetailAppointmentView(RetrieveUpdateDestroyAPIView):
    allowed_method = ["GET", "POST", "DELETE"]
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()


class ListMedicalNoteView(ListAPIView, CreateAPIView):
    allowed_method = ["GET", "POST"]
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()


class DetailMedicalNoteView(RetrieveUpdateDestroyAPIView):
    allowed_method = ["GET", "POST", "DELETE"]
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()