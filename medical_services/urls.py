from django.urls import path, include

from medical_services.apps import MedicalServicesConfig
from medical_services.views import index, MedicalCategoriesListView, MedicalCategoriesDetailView

app_name = MedicalServicesConfig.name

urlpatterns = [
    path('', index, name='home'),
    path('diagnostics/', MedicalCategoriesListView.as_view(), name='diagnostics'),
    path('diagnostics-detail/<int:pk>/', MedicalCategoriesDetailView.as_view(), name='diagnostics-detail'),
]
