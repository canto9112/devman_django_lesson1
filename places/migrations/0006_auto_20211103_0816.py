# Generated by Django 3.2.9 on 2021-11-03 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_auto_20211102_0715'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='place',
            options={},
        ),
        migrations.RemoveField(
            model_name='place',
            name='description_long',
        ),
    ]