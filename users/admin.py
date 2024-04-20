from django.contrib import admin

from users.models import User, MedicalStaff


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'email', 'phone', 'avatar', 'is_active', 'is_staff', 'first_name', 'last_name', 'is_superuser',)


@admin.register(MedicalStaff)
class MedicalStaffAdmin(admin.ModelAdmin):
    list_display = ('pk', 'employee', 'medical_category', 'medical_specialization', 'experience',)
