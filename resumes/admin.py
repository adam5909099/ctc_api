from django.contrib import admin
from .models import Position


class PositionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Position, PositionAdmin)
