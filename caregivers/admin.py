from django.contrib import admin
from .models import CareGiver
# Register your models here.


class CareGiverAdmin(admin.ModelAdmin):
    pass


admin.site.register(CareGiver, CareGiverAdmin)
