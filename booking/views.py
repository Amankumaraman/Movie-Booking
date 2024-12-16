from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime, timedelta
from .models import (
    Theater,
    Screen,
    Slot,
    WeeklyAvailability,
    WeeklyUnavailability,
    CustomUnavailability,
)
from .serializers import (
    WeeklyAvailabilitySerializer,
    WeeklyUnavailabilitySerializer,
    CustomUnavailabilitySerializer,
    SlotSerializer,
)


class TheaterAvailabilityViewSet(viewsets.ViewSet):
    """
    Handles weekly schedules and unavailability for theaters.
    """

    def create(self, request, pk=None):
        try:
            theater = Theater.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response(
                {"error": f"Theater with id {pk} does not exist."},
                status=status.HTTP_404_NOT_FOUND,
            )

        weekly_schedule = request.data.get("weekly_schedule", {})
        weekly_unavailability = request.data.get("weekly_unavailability", {})

        # Save weekly schedule
        for day, times in weekly_schedule.items():
            WeeklyAvailability.objects.create(
                theater=theater,
                day_of_week=day,
                open_time=times["open"],
                close_time=times["close"],
            )

        # Save weekly unavailability
        for day, times in weekly_unavailability.items():
            for time in times:
                WeeklyUnavailability.objects.create(
                    theater=theater,
                    day_of_week=day,
                    start_time=time["start"],
                    end_time=time["end"],
                )

        return Response({"status": "success", "message": "Theater availability updated successfully."}, status=status.HTTP_201_CREATED)


class CustomUnavailabilityViewSet(viewsets.ViewSet):
    """
    Handles custom unavailability for screens.
    """

    def create(self, request, pk=None):
        try:
            screen = Screen.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response(
                {"error": f"Screen with id {pk} does not exist."},
                status=status.HTTP_404_NOT_FOUND,
            )

        unavailable_slots = request.data.get("unavailable_slots", [])
        unavailable_dates = request.data.get("unavailable_dates", [])

        # Save custom unavailability for slots and dates
        for slot in unavailable_slots:
            CustomUnavailability.objects.create(
                screen=screen,
                date=slot["date"],
                start_time=slot["start"],
                end_time=slot["end"],
            )

        return Response({"status": "success", "message": "Custom unavailability saved successfully."}, status=status.HTTP_201_CREATED)


class AvailableSlotsViewSet(viewsets.ViewSet):
    """
    Fetches available slots for a screen between specified dates.
    """

    def list(self, request, pk=None):
        screen_id = request.query_params.get("screen_id")
        start_date = request.query_params.get("start_date")
        end_date = request.query_params.get("end_date")

        # Validate required parameters
        if not screen_id or not start_date or not end_date:
            return Response(
                {"error": "screen_id, start_date, and end_date are required parameters."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Parse dates
        try:
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
            end_date = datetime.strptime(end_date, "%Y-%m-%d")
        except ValueError:
            return Response(
                {"error": "Invalid date format. Use YYYY-MM-DD."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Fetch the screen
        try:
            screen = Screen.objects.get(id=screen_id)
        except ObjectDoesNotExist:
            return Response(
                {"error": f"Screen with id {screen_id} does not exist."},
                status=status.HTTP_404_NOT_FOUND,
            )

        # Generate slots
        slots = self.generate_slots(screen, start_date, end_date)

        serializer = SlotSerializer(slots, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def generate_slots(self, screen, start_date, end_date):
        """
        Generate slots for the given screen between the specified dates.
        """
        slots = []
        current_date = start_date
        while current_date <= end_date:
            slots.append(
                Slot(
                    screen=screen,
                    movie_name="Sample Movie",
                    start_time=current_date,
                    end_time=current_date + timedelta(hours=2),
                )
            )
            current_date += timedelta(hours=2)
        return slots
