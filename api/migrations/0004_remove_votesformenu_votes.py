# Generated by Django 4.2 on 2024-05-14 01:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_votesformenu_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='votesformenu',
            name='votes',
        ),
    ]
