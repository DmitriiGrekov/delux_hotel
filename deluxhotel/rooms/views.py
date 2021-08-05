from reservation.models import RoomModel
from django.views.generic.list import ListView
from django.db.models import Q


class AllRoomsView(ListView):
    template_name = 'rooms/list.html'
    context_object_name = 'rooms'
    paginate_by = 1

    def get_queryset(self):
        if self.request.method == 'GET':
            if self.request.GET.get('checkin'):
                check_in = self.request.GET.get('checkin')
                check_out = self.request.GET.get('checkout')
                room_type = self.request.GET.get('room_type')
                if room_type == 'Premium':
                    room_type = 'p'
                elif room_type == 'Basic':
                    room_type = 'b'
                adults = int(self.request.GET.get('adults'))
                kids = int(self.request.GET.get('kids'))
                max_people = str(adults + kids)
                email = self.request.GET.get('email')
                price_range = self.request.GET.get('price-range')
                self.request.session['check_in'] = check_in
                self.request.session['check_out'] = check_out
                self.request.session['email'] = email
                rooms = RoomModel.objects.filter(Q(room_type=room_type) & Q(max_people__gte=max_people) & Q(price__lte=price_range))
                return rooms
            else:
                return RoomModel.objects.filter(available=True)
