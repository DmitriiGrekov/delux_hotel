from django.contrib import admin
from .models import RoomModel, RoomModelReserved


@admin.register(RoomModel)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'room_size', 'available')
    list_display_links = ('name', 'price')


@admin.register(RoomModelReserved)
class RoomModelReserverdAdmin(admin.ModelAdmin):
    list_display = ('check_in', 'check_out', 'email', 'phone_number', 'room')
