from rest_framework import serializers
from .models import Trip, Subclub, TripRegistration

# class TripSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Trip
#         fields = ['title', 'tripLeader', 'date', 'attendees']


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ['id', 'trip_name', 'trip_date', 'trip_description', 'trip_leader', 'trip_capacity', 'subclub', 'trip_location', 'trip_provided', 'trip_bring', 'trip_type', 'trip_level']

class SubclubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subclub
        fields = ['id', 'subclub_name']

class TripRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripRegistration
        fields = ['id', 'student', 'trip']