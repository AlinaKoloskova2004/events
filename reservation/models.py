from django.db import models
from activity.models import Event
from django.contrib.auth.models import User


class Reservation(models.Model):
    status_choices = (
            ('Ожидание', 'Ожидание'),
            ('Подтверждено', 'Подтверждено'),
            ('Отклонено', 'Отклонено'),
        )
    event = models.ForeignKey(Event, on_delete=models.CASCADE,verbose_name='Мероприятие')
    reserved_places = models.IntegerField(default=0, verbose_name='Место бронирования')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    quantity = models.IntegerField(default=1, verbose_name='Кол-во мест')
    paid = models.BooleanField(default=False, verbose_name='Оплачиваемый')
    status = models.CharField(max_length=255, verbose_name='Статус', choices=status_choices)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, verbose_name='Итоговая сумма')

    def save(self, *args, **kwargs):
        self.total_price = self.event.price * self.quantity
        super().save(*args, **kwargs)