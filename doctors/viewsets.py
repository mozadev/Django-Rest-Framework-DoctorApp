from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import DoctorSerializer
from .models import Doctor

from rest_framework.permissions import IsAuthenticatedOrReadOnly


class DoctorViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(["POST"], detail=True, url_path="set-on-vacation")
    def set_on_vacation(self, request, pk):
        doctor = self.get_object()
        doctor.is_on_vacation = True
        doctor.save()
        return Response({"status": "Doctor is on vacations"})

    @action(["POST"], detail=True)
    def set_off_vacation(self, request, pk):
        doctor = self.get_object()
        doctor.is_on_vacation = False
        doctor.save()
        return Response({"status": "Doctor isn't on vacations"})
