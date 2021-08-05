from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.core.mail import send_mail
from reservation.models import RoomModel
from django.db.models import Max


class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['max_peoples'] = range(0, int(RoomModel.objects.aggregate(Max('max_people'))['max_people__max'])+1)
        context['room_type'] = ['Basic', 'Premium']
        return context


def contact_message(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        message = f"Сообщение от {name} - {email} \n {message} "
        send_mail('Contact message',
                  message,
                  'grekovdima7@gmail.com',
                  ['grekovdima7@gmail.com'])
        return redirect('main:index')
