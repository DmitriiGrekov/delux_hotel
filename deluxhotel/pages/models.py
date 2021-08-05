from django.db import models


class ContactMessageModel(models.Model):
    name = models.CharField(max_length=120, verbose_name='Имя')
    surname = models.CharField(max_length=120, verbose_name='Фамилия')
    phone = models.CharField(max_length=30, verbose_name='Телефон')
    note = models.TextField(verbose_name='Сообщение')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
