# Generated by Django 3.1.5 on 2021-08-29 10:10

from django.db import migrations
import recurrence.fields


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0007_auto_20210219_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='recurrences',
            field=recurrence.fields.RecurrenceField(default=''),
        ),
    ]