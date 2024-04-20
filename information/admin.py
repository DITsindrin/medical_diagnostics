from django.contrib import admin

from information.models import Contacts, Information


# Register your models here.
@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title',)


@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title',)
