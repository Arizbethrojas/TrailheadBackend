from rest_framework import serializers
from .models import Trip, Subclub, TripRegistration, Student, TripLeader, Waitlist, Enemies

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

### Changed - workaround for badges not showing right trip id
class TripRegistrationSerializer(serializers.ModelSerializer):
    trip_name = serializers.CharField(source='trip.trip_name')
    trip_date = serializers.DateField(source='trip.trip_date')
    trip_description = serializers.CharField(source='trip.trip_description')
    trip_leader = serializers.CharField(source='trip.trip_leader')
    subclub = serializers.SerializerMethodField()
    
    def get_subclub(self, obj):
        if obj.trip.subclub:
            if hasattr(obj.trip.subclub, 'subclub_name'):
                return obj.trip.subclub.subclub_name
            return obj.trip.subclub
        return None
    
    class Meta:
        model = TripRegistration
        fields = ['id', 'trip_name', 'trip_date', 'trip_description', 'trip_leader', 'subclub']

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
    class Meta:
        model = Enemies
        fields = ['id', 'complainer_id', 'receiver_id']

