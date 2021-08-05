from django.contrib import admin
from .models import ContactMessageModel


@admin.register(ContactMessageModel)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'phone')
    list_display_links = ('name', 'surname', 'phone')
