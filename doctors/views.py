from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)


from .models import (
    Doctor,
)


from .serializers import (
    DoctorSerializers,
)


class ListDoctorView(ListAPIView, CreateAPIView):
    """
    Get list of scheduled medical appointments
    """

    allowed_method = ["GET", "POST"]
    serializer_class = DoctorSerializers
    queryset = Doctor.objects.all()


class DetailDoctorsView(RetrieveUpdateDestroyAPIView):
    allowed_method = [
        "GET",
        "PUT",
        "DELETE",
    ]
    serializer_class = DoctorSerializers
    queryset = Doctor.objects.all()
