from rest_framework import serializers
from .models import Trip, Subclub, TripRegistration, Student, TripLeader, Waitlist, Enemies, Marker

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
    student_name = serializers.ReadOnlyField(source="student.student_name")
    class Meta:
        model = TripRegistration
        fields = ['id', 'student', 'trip', 'student_name']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'student_name', 'is_trip_leader', 'allergies', 'class_year', 'pronouns', 'profile_picture', 'favorite_subclubs']

class TripLeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripLeader
        fields = ['id', 'leader_name', 'leader_subclub']

class WaitlistSerializer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField(source='waitlist_student.student_name')
    class Meta:
        model = Waitlist
        fields = ['id', 'waitlist_student', 'waitlist_trip', 'student_name']

class EnemiesSerializer(serializers.ModelSerializer):
    blocked_name = serializers.ReadOnlyField(source='receiver_id.student_name')
    class Meta:
        model = Enemies
        fields = ['id', 'complainer_id', 'receiver_id', 'blocked_name']

class MarkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marker
        fields = ['id', 'latitude', 'longitude', 'image', 'created_at']


