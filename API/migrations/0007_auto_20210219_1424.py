# Generated by Django 3.1.5 on 2021-02-19 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0006_auto_20191025_0936'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='private',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='group',
            name='private',
            field=models.BooleanField(default=False),
        ),
    ]