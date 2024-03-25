from django.db import models
from activity.models import Event
from django.contrib.auth.models import User

class Reservation(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE,verbose_name='Мероприятие')
    reserved_places = models.IntegerField(default=0, verbose_name='Место бронирования')
    attendees = models.ManyToManyField(User, related_name='events_attending', verbose_name='Участник')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость')
    paid = models.BooleanField(default=False, verbose_name='Оплачиваемый')
    status = models.CharField(max_length=255, verbose_name='Статус')
