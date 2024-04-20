from django.urls import path, include

from registration_services.apps import RegistrationServicesConfig
from registration_services.views import MakeAppointmentCreateView, BackCallCreateView, MakeAppointmentListView, \
    success_message, success_message_call

app_name = RegistrationServicesConfig.name

urlpatterns = [
    path('call/', BackCallCreateView.as_view(), name='call'),
    path('<int:pk>/appointment/', MakeAppointmentCreateView.as_view(), name='registrations'),
    path('appointments/', MakeAppointmentListView.as_view(), name='appointments'),
    path('success_message/', success_message, name='success_message'),
    path('success_message_call/', success_message_call, name='success_message_call'),

]
