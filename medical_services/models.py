from django.db import models


# Create your models here.
class MedicalCategories(models.Model):
    """Модель категории медицинских услуг"""

    title = models.CharField(max_length=150, verbose_name='Наименование')
    abbreviated_title = models.CharField(max_length=150, verbose_name='Сокращенное наименование')
    description = models.TextField(verbose_name='Описание')
    preview = models.ImageField(upload_to='medical_services/', default='defauult.png', verbose_name='Превью')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class MedicalServices(models.Model):
    """Модель медицинских услуг"""

    medical_categories = models.ForeignKey(
        MedicalCategories, on_delete=models.CASCADE, verbose_name='Категория мед.услуг'
    )
    title = models.CharField(max_length=150, verbose_name='Медицинская услуга')
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')

    # Нужна ли тут связка с врачем?

    def __str__(self):
        return f'{self.title} - {self.price}'

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
