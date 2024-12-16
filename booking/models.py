from django.db import models
from django.utils import timezone


class Theater(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return self.name


class Screen(models.Model):
    theater = models.ForeignKey(Theater, related_name="screens", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.theater.name} - {self.name}"


class Slot(models.Model):
    screen = models.ForeignKey(Screen, related_name="slots", on_delete=models.CASCADE)
    movie_name = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.movie_name} - {self.start_time} to {self.end_time}"


class WeeklyAvailability(models.Model):
    theater = models.ForeignKey(Theater, related_name="weekly_availabilities", on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=9)  # e.g., Monday
    open_time = models.TimeField()
    close_time = models.TimeField()

    def __str__(self):
        return f"{self.theater.name} - {self.day_of_week}"


class WeeklyUnavailability(models.Model):
    theater = models.ForeignKey(Theater, related_name="weekly_unavailabilities", on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=9)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.theater.name} - Unavailability on {self.day_of_week}"


class CustomUnavailability(models.Model):
    screen = models.ForeignKey(Screen, related_name="custom_unavailabilities", on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.screen.name} - Unavailability on {self.date} from {self.start_time} to {self.end_time}"
