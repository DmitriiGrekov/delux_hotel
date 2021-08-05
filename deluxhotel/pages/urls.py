from django.urls import path
from .views import (AboutView, 
                    ContactView,
                    FaqView)

app_name = 'pages'
urlpatterns = [
    path('', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('faq/', FaqView.as_view(), name='faq'),
]
