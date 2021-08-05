from django.dispatch import Signal
from django.core.mail import send_mail

send_messages = Signal(providing_args=['email_to',
                                       'room',
                                       'check_in',
                                       'check_out',
                                       'first_name',
                                       'last_name'])


def send_messages_dispatch(sender, **kwargs):
    subject = "Successed reverser room"
    message = f"Dear {kwargs['first_name']} {kwargs['last_name']}. \
                You have successfully reserved room - {kwargs['room'].name}.\
                Check-in date - {kwargs['check_in']} , \
                Check-out date - {kwargs['check_out']} "
    send_mail(subject, message, 'grekovdima7@gmail.com', [kwargs['email_to']])


send_messages.connect(send_messages_dispatch)
