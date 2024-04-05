from django.db import models
from activity.models import Event
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.core.mail import send_mail


class Reservation(models.Model):
    status_choices = (
              ('ожидание', 'Ожидание'),
              ('подтверждено', 'Подтверждено'),
              ('отменено', 'Отменено'),
        )
    event = models.ForeignKey(Event, on_delete=models.CASCADE,verbose_name='Мероприятие')
    reserved_places = models.IntegerField(default=0, verbose_name='Место бронирования')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    quantity = models.IntegerField(default=1, verbose_name='Кол-во мест')
    paid = models.BooleanField(default=False, verbose_name='Оплачиваемый')
    status = models.CharField(max_length=255, verbose_name='Статус', choices=status_choices, default='ожидание')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, verbose_name='Итоговая сумма')

    def save(self, *args, **kwargs):
        self.total_price = self.event.price * self.quantity
        super().save(*args, **kwargs)

@receiver(pre_save, sender=Reservation)
def save_reservation_status(sender, instance, **kwargs):
    if instance.pk:
        db_instance = Reservation.objects.get(pk=instance.pk)
        instance._old_status = db_instance.status
    else:
        instance._old_status = instance.status

@receiver(post_save, sender=Reservation)
def send_notification(sender, instance, created, **kwargs):
    if created or instance.status != instance._old_status:
        subject = 'Изменение статуса бронирования'
        message = f'Статус бронирования был изменен на {instance.status}.'
        send_mail(subject, message, 'allevents.com', [instance.user.email])