from django.contrib import admin
from .models import Race, RaceData, RaceTiming


class RaceDataInline(admin.TabularInline):
    model = RaceData
    extra = 1
    fields = ('bib', 'name', 'country', 'gender', 'category', 'age')


class RaceTimingInline(admin.TabularInline):
    model = RaceTiming
    extra = 1
    fields = ('checkpoint_number', 'timestamp')
    readonly_fields = ('timestamp', )


@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    list_display = ('race_name', 'race_date', 'location')
    search_fields = ('race_name', 'location')
    list_filter = ('race_date', )
    inlines = [RaceDataInline]

    def create_race_data(self, request, obj):
        # Example custom admin action, if desired
        pass


@admin.register(RaceData)
class RaceDataAdmin(admin.ModelAdmin):
    list_display = ('bib', 'name', 'country', 'gender', 'category', 'age',
                    'race')
    search_fields = ('bib', 'name', 'country')
    list_filter = ('gender', 'country', 'category', 'race')
    ordering = ('race', 'bib')
    inlines = [RaceTimingInline]


@admin.register(RaceTiming)
class RaceTimingAdmin(admin.ModelAdmin):
    list_display = ('runner', 'checkpoint_number', 'timestamp')
    search_fields = ('runner__race_name', )
    list_filter = ('checkpoint_number', 'runner')
    ordering = ('runner', 'checkpoint_number')
    autocomplete_fields = ('runner', )
