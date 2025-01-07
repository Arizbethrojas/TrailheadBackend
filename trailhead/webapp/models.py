from django.db import models
from django.contrib.auth.models import User

# Django provides an object relational mapping (ORM)
# allows us to write python code to create database models and 
# then those models are AUTOMATICALLY created for us in SQL light 3 
# we make a migration, which is automated code, which creates the corresponding model in SQL or mongoDB

class TodoItem(models.Model): 
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

class Subclub(models.Model):
    subclub_name = models.CharField(max_length=255)

    def __str__(self):
        return self.subclub_name

class Trip(models.Model):

    TRIP_TYPE_CHOICES = [
        ('day_trip', 'Day Trip'),
        ('overnight_trip', 'Overnight')
    ]

    TRIP_LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    trip_name = models.CharField(max_length=255)
    trip_date = models.DateField()
    trip_description = models.TextField()
    trip_leader = models.CharField(max_length=255)
    trip_capacity = models.IntegerField()
    subclub = models.ForeignKey(Subclub, on_delete=models.CASCADE)
    trip_location = models.CharField(max_length=255)
    trip_provided = models.TextField()
    trip_bring = models.TextField()
    trip_type = models.CharField(max_length=20, choices=TRIP_TYPE_CHOICES)
    trip_level = models.CharField(max_length=20, choices=TRIP_LEVEL_CHOICES)

    def __str__(self):
        return self.trip_name

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=255)
    is_trip_leader = models.BooleanField(default=False)
    def __str__(self):
        return self.student_name

class TripRegistration(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)

class Waitlist(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)

