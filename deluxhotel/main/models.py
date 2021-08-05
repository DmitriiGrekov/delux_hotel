from django.db import models


class ContactInfoModel(models.Model):
    adress = models.CharField(max_length=150, verbose_name='Адрес')
    email = models.EmailField(verbose_name='Почта')
    phone = models.CharField(max_length=30, verbose_name='Телефон')

    class Meta:
        verbose_name = 'Контакт для связи'
        verbose_name_plural = 'Контакты для связи'
