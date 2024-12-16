from rest_framework import serializers
from .models import Theater, Screen, Slot, WeeklyAvailability, WeeklyUnavailability, CustomUnavailability


class WeeklyAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = WeeklyAvailability
        fields = '__all__'


class WeeklyUnavailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = WeeklyUnavailability
        fields = '__all__'


class CustomUnavailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUnavailability
        fields = '__all__'


class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slot
        fields = ['id', 'movie_name', 'start_time', 'end_time', 'screen']
