from django.db import models
from activity.models import Event
from django.contrib.auth.models import User

class Reservation(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE,verbose_name='Мероприятие')
    name = models.CharField(max_length=255, verbose_name='ФИО')
    email = models.CharField(max_length=255, verbose_name='Почта')
    reserved_places = models.IntegerField(default=0, verbose_name='Место бронирования')
    attendees = models.ManyToManyField(User, related_name='events_attending', verbose_name='Участник')
    quantity = models.IntegerField(default=1, verbose_name='Кол-во')
    paid = models.BooleanField(default=False, verbose_name='Оплачиваемый')
    status = models.CharField(max_length=255, verbose_name='Статус')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, verbose_name='Итоговая сумма')

    def save(self, *args, **kwargs):
        self.total_price = self.event.price * self.quantity
        super().save(*args, **kwargs)