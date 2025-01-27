from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Student

#listens for post_save signal, meaning a new user was just created! so it is time to create a student 
@receiver(post_save, sender=User)
def create_student_profile(sender, instance, created, **kwargs):
    """Automatically create a Student profile when a User is created."""
    if created:
        Student.objects.create(user=instance, student_name=instance.username)

@receiver(post_save, sender=User)
def save_student_profile(sender, instance, **kwargs):
    """Save the Student profile when the User is saved."""
    try:
        # Update or save the Student profile if it's already linked
        instance.student.save()
    except Student.DoesNotExist:
        pass
