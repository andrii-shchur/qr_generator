# Generated by Django 4.0.1 on 2022-02-04 21:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_rename_user_id_qrcode_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='qrcode',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 4, 21, 57, 13, 358333, tzinfo=utc)),
        ),
    ]