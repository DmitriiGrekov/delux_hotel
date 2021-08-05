from django.db import models


class RoomModel(models.Model):
    ROOM_TYPE = (
        ('b', 'Basic'),
        ('p', 'Premium')
    )
    WIFI_CHOICES = (
        ('a', 'Available'),
        ('n', 'No available')
    )
    ROOM_SERVICE_CHOICES = (
        ('a', 'Available'),
        ('n', 'No available')
    )
    BREAKFAST_CHOICES = (
        ('i', 'Included'),
        ('n', 'Not included')
    )
    LAYNDRY_CHOICES = (
        ('a', 'Available'),
        ('n', 'No available')
    )
    TAXI_TO_AIRPORT_CHOICES = (
        ('y', 'Yes'),
        ('n', 'No')
    )
    name = models.CharField(max_length=120, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    room_type = models.CharField(max_length=120,
                                 verbose_name='Тип комнаты',
                                 choices=ROOM_TYPE, default='b')
    image = models.ImageField(verbose_name='Картинка', blank=True, null=True)
    price = models.FloatField(verbose_name='Цена')
    room_size = models.IntegerField(verbose_name='Размер комнаты',
                                    blank=True,
                                    null=True)
    bed = models.IntegerField(verbose_name='Колличество кроватей',
                              blank=True,
                              null=True)
    max_people = models.IntegerField(verbose_name='Максимальное колличество людей',
                                     blank=True, null=True)
    wifi = models.CharField(max_length=120,
                            choices=WIFI_CHOICES,
                            verbose_name='Wifi')
    room_service = models.CharField(max_length=120,
                                    choices=ROOM_SERVICE_CHOICES,
                                    verbose_name='Уборка комнат')
    breakfast = models.CharField(max_length=120,
                                 choices=BREAKFAST_CHOICES,
                                 verbose_name='Завтрак')
    layndry = models.CharField(max_length=120,
                               choices=LAYNDRY_CHOICES,
                               verbose_name='Прачечная')
    taxi = models.CharField(max_length=120,
                            choices=TAXI_TO_AIRPORT_CHOICES,
                            verbose_name='Такси до аэропорта')
    available = models.BooleanField(default=True, verbose_name='Свободен?')

    def wifi_choices(self):
        return dict(RoomModel.WIFI_CHOICES)[self.wifi]

    def room_service_choices(self):
        return dict(RoomModel.ROOM_SERVICE_CHOICES)[self.room_service]

    def breakfast_choices(self):
        return dict(RoomModel.BREAKFAST_CHOICES)[self.breakfast]

    def layndry_choices(self):
        return dict(RoomModel.LAYNDRY_CHOICES)[self.layndry]

    def taxi_choices(self):
        return dict(RoomModel.TAXI_TO_AIRPORT_CHOICES)[self.taxi]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'


class RoomModelReserved(models.Model):
    first_name = models.CharField(max_length=120, verbose_name='Имя')
    last_name = models.CharField(max_length=120, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='Почта')
    phone_number = models.CharField(max_length=30, verbose_name='Телефон')
    additional_node = models.TextField(verbose_name='Дополнительное примечание')
    check_in = models.DateField(verbose_name='Дата заселения', null=True)
    check_out = models.DateField(verbose_name='Дата выселения', null=True)
    room = models.ForeignKey('RoomModel',
                             on_delete=models.PROTECT,
                             related_name='room',
                             null=True)

    class Meta:
        verbose_name = 'Посетитель'
        verbose_name_plural = 'Зарезервированные комнаты'
