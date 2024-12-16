from django.contrib import admin
from .models import Theater, Screen, Slot, WeeklyAvailability, WeeklyUnavailability, CustomUnavailability


@admin.register(Theater)
class TheaterAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "address")
    search_fields = ("name", "address")
    ordering = ("name",)
    list_per_page = 20


@admin.register(Screen)
class ScreenAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "theater")
    search_fields = ("name", "theater__name")
    list_filter = ("theater",)
    ordering = ("theater__name", "name")
    list_per_page = 20


@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    list_display = ("id", "screen", "movie_name", "start_time", "end_time")
    search_fields = ("movie_name", "screen__name", "screen__theater__name")
    list_filter = ("screen__theater", "screen")
    ordering = ("start_time",)
    list_per_page = 20


@admin.register(WeeklyAvailability)
class WeeklyAvailabilityAdmin(admin.ModelAdmin):
    list_display = ("id", "theater", "day_of_week", "open_time", "close_time")
    search_fields = ("theater__name", "day_of_week")
    list_filter = ("day_of_week", "theater")
    ordering = ("theater__name", "day_of_week")
    list_per_page = 20


@admin.register(WeeklyUnavailability)
class WeeklyUnavailabilityAdmin(admin.ModelAdmin):
    list_display = ("id", "theater", "day_of_week", "start_time", "end_time")
    search_fields = ("theater__name", "day_of_week")
    list_filter = ("day_of_week", "theater")
    ordering = ("theater__name", "day_of_week")
    list_per_page = 20


@admin.register(CustomUnavailability)
class CustomUnavailabilityAdmin(admin.ModelAdmin):
    list_display = ("id", "screen", "date", "start_time", "end_time")
    search_fields = ("screen__name", "screen__theater__name", "date")
    list_filter = ("date", "screen", "screen__theater")
    ordering = ("date", "screen__name")
    list_per_page = 20
