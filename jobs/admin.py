from django.contrib import admin
from .models import Position, Job


class PositionAdmin(admin.ModelAdmin):
    pass


class JobAdmin(admin.ModelAdmin):
    pass


admin.site.register(Position, PositionAdmin)
admin.site.register(Job, JobAdmin)
