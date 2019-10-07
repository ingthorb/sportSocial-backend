from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=50, default="")
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Cities'


class Sport(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Sports'


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
        return self.username

    class Meta:
        ordering = ['created_at']
        verbose_name_plural = 'Users'


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
    difficulty = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Events'


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event

    class Meta:
        ordering = ['created_at']


class Group(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField('User')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Groups'
