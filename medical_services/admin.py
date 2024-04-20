from django.contrib import admin

from medical_services.models import MedicalCategories, MedicalServices


# Register your models here.
@admin.register(MedicalCategories)
class MedicalCategoriesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description',)


@admin.register(MedicalServices)
class MedicalServicesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'medical_categories', 'price',)
