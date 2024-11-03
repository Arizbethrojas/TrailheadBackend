from django.db import models

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
    trip_name = models.CharField(max_length=255)
    trip_date = models.DateField()
    trip_description = models.TextField()
    trip_leader = models.CharField(max_length=255)
    trip_capacity = models.IntegerField()
    subclub = models.ForeignKey(Subclub, on_delete=models.CASCADE)

    def __str__(self):
        return self.trip_name

class Student(models.Model):
    student_name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.student_name

class TripRegistration(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)

class Waitlist(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)