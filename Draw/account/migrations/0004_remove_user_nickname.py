# Generated by Django 4.2.4 on 2023-08-18 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_rename_user_id_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='nickname',
        ),
    ]
