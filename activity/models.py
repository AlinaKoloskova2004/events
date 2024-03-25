from django.db import models


# Create your models here.
class Event(models.Model):
    type = models.CharField(max_length=255, verbose_name='Тип мероприятия')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    date = models.DateField(verbose_name='Дата')
    places = models.IntegerField(default=0)
    time = models.TimeField(verbose_name='Время')
    location = models.CharField(max_length=255, verbose_name='Место')
    organizer = models.CharField(max_length=255, verbose_name='Орагнизатор')
    image = models.ImageField(upload_to='event_images/', verbose_name='Изображение')

    def __str__(self):
        return self.title