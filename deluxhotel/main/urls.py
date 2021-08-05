from django.urls import path
from .views import IndexView
from .views import contact_message


app_name = 'main'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('send_message/', contact_message, name='send_message'),
]
