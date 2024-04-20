from django.contrib import admin

from registration_services.models import MakeAppointment, BackCall


# Register your models here.
@admin.register(MakeAppointment)
class MakeAppointmentAdmin(admin.ModelAdmin):
    list_display = ("patient", 'medical_services', 'doctor_id', 'date_creation', 'date_reception',)


@admin.register(BackCall)
class BackCallAdmin(admin.ModelAdmin):
    list_display = ("phone", 'last_name',)
