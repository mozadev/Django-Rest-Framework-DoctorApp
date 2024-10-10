from django.urls import path

from .views import detail_patient, ListPatientsView, DetailPatientsView

urlpatterns = [
    # path('patients', list_patients),
    # path('patients/<int:pk>/', detail_patient)
    path('patients', ListPatientsView.as_view()),
    path('patients/<int:pk>/', DetailPatientsView.as_view())
]