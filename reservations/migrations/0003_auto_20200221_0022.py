# Generated by Django 2.2.5 on 2020-02-20 22:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_auto_20200221_0021'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='status11',
            new_name='status',
        ),
    ]
