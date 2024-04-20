from django.db import models

from medical_services.models import MedicalServices
from users.models import User, MedicalStaff


# Делаю запись через прием заявкия с данными пользователя

class BackCall(models.Model):
    """Модель Обратный звонок"""

    phone = models.CharField(max_length=75, verbose_name='Телефон')
    last_name = models.CharField(max_length=75, verbose_name='Имя пациента')

    def __str__(self):
        return f'{self.phone} - {self.last_name}'

    class Meta:
        verbose_name = 'Обратный звонок'
        verbose_name_plural = 'Обратные звонки'
        ordering = ('pk',)


class MakeAppointment(models.Model):
    """Модель Запись на прием"""

    patient = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пациент')
    medical_services = models.ForeignKey(
        MedicalServices, on_delete=models.CASCADE, verbose_name='Медицинская услуга'
    )

    doctor = models.ForeignKey(MedicalStaff, on_delete=models.CASCADE, verbose_name='Врач')
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания записи')
    date_reception = models.DateTimeField(verbose_name='Дата и время приема')

    anonymous_phone = models.CharField(
        max_length=75, null=True, blank=True, verbose_name='Телефон неавторизованного пользователя'
    )
    anonymous_first_name = models.CharField(
        max_length=75, null=True, blank=True, verbose_name='Имя неавторизованного пользователя'
    )
    anonymous_last_name = models.CharField(
        max_length=75, null=True, blank=True, verbose_name='Фамилия неавторизованного пользователя'
    )

    def __str__(self):
        return f'{self.patient} - {self.medical_services} - {self.date_creation} - {self.date_reception} {self.anonymous_first_name} - {self.anonymous_phone}'

    class Meta:
        verbose_name = 'Запись на прием'
        verbose_name_plural = 'Записи на приемы'
        ordering = ('date_reception',)
