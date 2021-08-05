from django.urls import path
from .views import AllRoomsView

app_name = 'rooms'
urlpatterns = [
    path('', AllRoomsView.as_view(), name='list'),
]
