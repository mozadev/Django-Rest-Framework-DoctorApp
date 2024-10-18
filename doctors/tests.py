from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from patients.models import Patient
from doctors.models import Doctor


# Create your tests here.
class DoctorViewSetTest(TestCase):

    def setUp(self):
        self.patient = Patient.objects.create(
            first_name="Jose",
            last_name="Perez",
            date_of_birth="1990-12-05",
            contact_number="12312312",
            email="example@example",
            address="Address test",
            medical_history="Any",
        )
        self.doctor = Doctor.objects.create(
            first_name="Maria",
            last_name="Torres",
            qualification="Professional",
            contact_number="12313456",
            email="example2@example",
            address="Lima",
            biography="Any",
            is_on_vacation=False,
        )
        self.client = APIClient()

    def test_list_should_return_200(self):
        url = reverse(
            "doctor-appointments",
            kwargs={"pk": self.doctor.id},
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
