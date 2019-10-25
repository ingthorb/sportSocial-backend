# Generated by Django 2.2.6 on 2019-10-25 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0005_auto_20191025_0914'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='lat',
            field=models.DecimalField(decimal_places=7, default=14.22, max_digits=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='long',
            field=models.DecimalField(decimal_places=7, default=13.22, max_digits=12),
            preserve_default=False,
        ),
    ]