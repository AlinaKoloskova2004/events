# Generated by Django 5.0.3 on 2024-03-24 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0002_remove_event_attendees_event_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='price',
        ),
    ]