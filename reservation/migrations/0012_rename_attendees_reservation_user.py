# Generated by Django 5.0.3 on 2024-04-02 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0011_remove_reservation_attendees_reservation_attendees'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='attendees',
            new_name='user',
        ),
    ]