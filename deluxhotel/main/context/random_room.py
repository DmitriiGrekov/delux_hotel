from reservation.models import RoomModel


def random_room(request):
    context = {}
    context['random_room'] = RoomModel.objects.all().order_by('?')[:3]
    return context
