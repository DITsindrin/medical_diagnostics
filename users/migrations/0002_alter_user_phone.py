# Generated by Django 4.2.7 on 2024-04-20 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=25, verbose_name='Телефон'),
        ),
    ]