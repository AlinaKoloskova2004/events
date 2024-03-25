from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission

class CustomUser(AbstractUser):
    username = models.CharField(max_length=255, verbose_name='Логин')
    surname = models.CharField(max_length=255, verbose_name='Фамилия')
    name = models.CharField(max_length=255, verbose_name='Имя')
    email = models.CharField(max_length=255, verbose_name='Почта')
    password1 = models.CharField(max_length=255, verbose_name='Пароль')
    password2 = models.CharField(max_length=255, verbose_name='Повтор пароля')
    email_confirmed = models.BooleanField(default=False, verbose_name='Подтверждён')
    groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_user_permissions')

