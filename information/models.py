from django.db import models


# Create your models here.
class Contacts(models.Model):
    """Модель контактов"""
    title = models.CharField(max_length=150, verbose_name='Наименование')
    opening_hours = models.CharField(max_length=100, verbose_name='Часы работы')
    address = models.CharField(max_length=250, verbose_name='Адрес')
    phone = models.CharField(max_length=75, verbose_name='Телефон')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Information(models.Model):
    """Модель иформация"""
    title = models.CharField(max_length=150, verbose_name='Название')
    info = models.TextField(verbose_name='Информация')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Информация'
        verbose_name_plural = 'Информации'
        ordering = ('pk',)
