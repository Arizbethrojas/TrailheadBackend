from rest_framework import serializers
from .models import Trip, Subclub, TripRegistration, Student, TripLeader, Waitlist, Enemies, Notification

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

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'student_name', 'is_trip_leader', 'allergies', 'class_year', 'pronouns', 'profile_picture', 'favorite_subclubs']


class TripLeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripLeader
        fields = ['id', 'leader_name', 'leader_subclub']

class WaitlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waitlist
        fields = ['id', 'waitlist_student', 'waitlist_trip']

class EnemiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enemies
        fields = ['id', 'complainer_id', 'receiver_id']

