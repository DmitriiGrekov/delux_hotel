from django.contrib import admin
from .models import ContactInfoModel


@admin.register(ContactInfoModel)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('adress', 'email', 'phone')
    list_editable = ('email', 'phone')
