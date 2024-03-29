from django.db import models
from recurrence.fields import RecurrenceField

class Country(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=50, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Cities'

    def __unicode__(self):
        return self.name


class Sport(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Sports'

    def __unicode__(self):
        return self.name


class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    email = models.EmailField()
    age = models.IntegerField()

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        ordering = ['created_at']
        verbose_name_plural = 'Users'

    def __unicode__(self):
        return self.username


# Add recurring field to offer users how often they would want it to happen
class Event(models.Model):
    name = models.CharField(max_length=50)
    users = models.ManyToManyField('User')
    description = models.TextField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    recurrences = RecurrenceField(default='')
    long = models.DecimalField(max_digits=12, decimal_places=7)
    lat = models.DecimalField(max_digits=12, decimal_places=7)
    difficulty = models.CharField(max_length=100)
    private = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Events'

    def __unicode__(self):
        return self.name


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s: %s' % (self.user, self.text)

    class Meta:
        ordering = ['created_at']

    def __unicode__(self):
        return self.text


class Group(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField('User')
    private = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Groups'
