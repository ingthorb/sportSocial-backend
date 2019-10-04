from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=100, blank=True, default='')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    description = models.TextField()
    created = models.DateTimeField()

    class Meta:
        app_label = 'backend'
        ordering = ['created']


class Sport(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()

    class Meta:
        app_label = 'backend'


class Country(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        app_label = 'backend'


class Event(models.Model):
    name = models.CharField(max_length=50)
    users = models.ForeignKey(User, on_delete=models.PROTECT)
    created = models.DateTimeField()

    class Meta:
        app_label = 'backend'


class Group(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    created = models.DateTimeField()

    class Meta:
        app_label = 'backend'
