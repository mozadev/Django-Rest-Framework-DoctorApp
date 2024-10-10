from .serializers import PatientSerializer
from .models import Patient

# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

# GET /api/patients => list
# POST /api/patients => Create
# GET /api/patients/<pk>/ => Detail
# PUT /api/patients/<pk> => Modify
# DELETE /api/patients/<pk> => Modify


class ListPatientsView(ListAPIView, CreateAPIView):
    allowed_methods = ["GET", "POST"]
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()


class DetailPatientsView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ["GET", "PUT", "DELETE"]
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()


# class ListPatientsView(APIView):
#     allowed_methods = ["GET", "POST"]

#     def get(self, request):
#         patients = Patient.objects.all()
#         serializer = PatientSerializer(patients, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = PatientSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(status=status.HTTP_201_CREATED)


# class DetailPatientsView(APIView):
#     allowed_methods = ["GET", "PUT", "DELETE"]

#     def get(self, request, pk):
#         try:
#             patient = Patient.objects.get(id=pk)
#         except Patient.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = PatientSerializer(patient)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         try:
#             patient = Patient.objects.get(id=pk)
#         except Patient.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = PatientSerializer(patient, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

#     def delete(self, request, pk):
#         try:
#             patient = Patient.objects.get(id=pk)
#         except Patient.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         patient.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(["GET", "POST"])
# def list_patients(request):
#     if request.method == "GET":
#         patients = Patient.objects.all()
#         serializer = PatientSerializer(patients, many=True)
#         return Response(serializer.data)

#     if request.method == "POST":
#         serializer = PatientSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(status=status.HTTP_201_CREATED)


# @api_view(["GET", "PUT", "DELETE"])
# def detail_patient(request, pk):
#     try:
#         patient = Patient.objects.get(id=pk)
#     except Patient.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":
#         serializer = PatientSerializer(patient)
#         return Response(serializer.data)

#     if request.method == "PUT":
#         serializer = PatientSerializer(patient, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

#     if request.method == "DELETE":
#         patient.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)   