from main.models import ContactInfoModel


def contact_info(request):
    context = {'contact_info': ContactInfoModel.objects.first()}
    return context
