from django.contrib.auth.models import AbstractUser, Group
from django.db import models

from medical_services.models import MedicalCategories

# Create your models here.
ROLE = [('admin', 'ADMIN'), ('doctor', 'DOCTOR'), ('patient', 'PATIENT'), ('manager', 'MANAGER')]


class User(AbstractUser):
    """Модель пользователя"""

    username = None

    email = models.EmailField(unique=True, verbose_name='Email')
    phone = models.CharField(unique=True, max_length=25, verbose_name='Телефон')
    surname = models.CharField(max_length=75, verbose_name='Отчество')
    avatar = models.ImageField(upload_to='users/', default='users.png', verbose_name='Аватар')
    role = models.CharField(max_length=15, choices=ROLE, default='patient', verbose_name='Роль пользователя')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class MedicalStaff(models.Model):
    """Модель сотрудника"""

    employee = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Сотрудник')
    medical_category = models.ForeignKey(
        MedicalCategories,
        on_delete=models.SET_DEFAULT,
        default='No medical category',
        verbose_name='Медицинская категория'
    )
    medical_specialization = models.CharField(max_length=500, verbose_name='Медицинская специализация')
    experience = models.CharField(max_length=50, verbose_name='Стаж работы')
    # role = models.CharField(max_length=15, choices=ROLE, default='patient', verbose_name='Роль пользователя')

    def __str__(self):
        return f'{self.employee} - {self.medical_specialization} - {self.medical_category} - {self.experience}'

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
