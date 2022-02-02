from django.contrib import admin
from apps.customapi.models import Calendar

class CalendarAdmin(admin.ModelAdmin):
    list_display = ['user', 'start_date', 'end_date']    

admin.site.register(Calendar, CalendarAdmin)