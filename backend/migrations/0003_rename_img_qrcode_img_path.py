# Generated by Django 4.0.1 on 2022-02-04 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_alter_qrcode_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='qrcode',
            old_name='img',
            new_name='img_path',
        ),
    ]
