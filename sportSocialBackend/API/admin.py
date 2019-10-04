from django.contrib import admin
from API.models import User, Sport, Group, Country, Event, City


class UserAdmin(admin.ModelAdmin):
    fields = ['username', 'first_name', 'last_name', 'description', 'created', 'country']


admin.site.register(User, UserAdmin)
admin.site.register(Sport)
admin.site.register(Group)
admin.site.register(Country)
admin.site.register(Event)
admin.site.register(City)
