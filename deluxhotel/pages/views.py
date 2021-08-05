from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import ContactMessageForm
from .models import ContactMessageModel


class AboutView(TemplateView):
    template_name = 'pages/about.html'


class ContactView(SuccessMessageMixin, CreateView):
    template_name = 'pages/contact.html'
    form_class = ContactMessageForm
    model = ContactMessageModel
    success_url = reverse_lazy('pages:contact')
    success_message = 'Ваш отзыв успешно отправлен'


class FaqView(TemplateView):
    template_name = 'pages/faq.html'
