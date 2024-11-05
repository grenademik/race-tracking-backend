# api/admin.py
from django.contrib import admin
from .models import Race, RaceData, RaceTiming

admin.site.register(Race)
admin.site.register(RaceData)
admin.site.register(RaceTiming)
