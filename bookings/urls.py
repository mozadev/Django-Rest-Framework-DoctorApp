from django.urls import path

from .views import (
    ListAppointmentView,
    ListMedicalNoteView,
    DetailAppointmentView,
    DetailMedicalNoteView,
)

urlpatterns = [
    path("appointment", ListAppointmentView.as_view()),
    path("appointment/<int:id>/", DetailAppointmentView.as_view()),
    path("medicalnotes", ListMedicalNoteView.as_view()),
    path("medicalnotes/<int:id>/", DetailMedicalNoteView.as_view()),
]
