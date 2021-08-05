from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import Q
from django.db.models import Max
from .models import RoomModel, RoomModelReserved
from .forms import RoomModelReservedForm
from .signals.messages import send_messages
import datetime


class RoomsListView(ListView):
    template_name = 'reservation/list.html'
    paginate_by = 2
    context_object_name = 'rooms'

    def get_queryset(self):
        if self.request.GET.get('kids') and self.request.GET.get('adults'):
            kids = int(self.request.GET.get('kids'))
            adults = int(self.request.GET.get('adults'))
            all = kids+adults
            self.request.session['check_in'] = self.request.GET.get('checkin')
            self.request.session['check_out'] = self.request.GET.get('checkout')
            return RoomModel.objects.filter(Q(max_people__gte=all) & Q(available=True))
        else:
            return RoomModel.objects.filter(available=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['people_adults'] = range(1, int(RoomModel.objects.aggregate(Max('max_people'))['max_people__max'])+1)
        context['people_kids'] = range(0, int(RoomModel.objects.aggregate(Max('max_people'))['max_people__max'])+1)
        return context


def reserved_view(request, room):
    if request.method == "POST":
        form = RoomModelReservedForm(request.POST)
        if form.is_valid():
            room = get_object_or_404(RoomModel, pk=room)
            room_reverse = RoomModelReserved()
            check_in = request.session.get('check_in')
            check_out = request.session.get('check_out')
            if check_in and check_out:
                room_reverse.first_name = form.cleaned_data['first_name']
                room_reverse.last_name = form.cleaned_data['last_name']
                room_reverse.email = form.cleaned_data['email']
                room_reverse.phone_number = form.cleaned_data['phone_number']
                room_reverse.additional_node = form.cleaned_data['additional_node']
                room_reverse.check_in = datetime.datetime.strptime(check_in, "%d-%m-%Y").date()
                room_reverse.check_out = datetime.datetime.strptime(check_out, "%d-%m-%Y").date()
                room_reverse.room = room
                room_reverse.save()
                del request.session['check_in']
                del request.session['check_out']
                room.available = False
                room.save()
                send_messages.send(request,
                                   email_to=form.cleaned_data['email'],
                                   room=room,
                                   check_in=check_in,
                                   check_out=check_out,
                                   first_name=form.cleaned_data['first_name'],
                                   last_name=form.cleaned_data['last_name'])
                return render(request, 'reservation/reserved_room_done.html')

    else:
        form = RoomModelReservedForm()
        context = {'form': form}
        return render(request, 'reservation/reserved_room.html', context)


class RoomDetailView(DetailView):
    model = RoomModel
    template_name = 'reservation/detail.html'
    context_object_name = 'room'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_rooms'] = RoomModel.objects.filter(~Q(pk=kwargs['object'].pk)).filter(available=True)
        return context
