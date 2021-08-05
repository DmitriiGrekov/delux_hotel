from django.urls import path
from .views import RoomsListView, RoomDetailView
from .views import reserved_view


app_name = 'reservation'
urlpatterns = [
    path('', RoomsListView.as_view(), name='list'),
    path('<int:pk>/', RoomDetailView.as_view(), name='detail'),
    path('<int:room>/reserve/', reserved_view, name='reserve'),
]
