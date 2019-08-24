from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Event, EventType

class EventAdmin(admin.ModelAdmin):
    pass

class EventTypeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Event, EventAdmin)
admin.site.register(EventType, EventTypeAdmin)