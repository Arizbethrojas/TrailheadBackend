from rest_framework import serializers
from .models import Trip

# class TripSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Trip
#         fields = ['title', 'tripLeader', 'date', 'attendees']


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ['id', 'trip_name', 'trip_date', 'trip_description', 'trip_leader', 'trip_capacity', 'subclub']