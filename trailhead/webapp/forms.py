# your_app/forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Student 

from django.core.exceptions import ValidationError

class FullSignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class_year = forms.CharField(max_length=4, required=False)
    allergies = forms.CharField(widget=forms.Textarea, required=False)
    pronouns = forms.CharField(max_length=50, required=False)
    is_trip_leader = forms.BooleanField(required=False)
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        print(f"Cleaned Data: {self.cleaned_data}")  # Debugging line to check what Django sees

        # Create the user object
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()

        # Create the associated Student object
        try:
            student = Student.objects.create(
                user=user,
                allergies=self.cleaned_data.get('allergies', ''),
                class_year=self.cleaned_data.get('class_year', ''),
                pronouns=self.cleaned_data.get('pronouns', ''),
                is_trip_leader=self.cleaned_data.get('is_trip_leader', False),
                profile_picture=self.cleaned_data.get('profile_picture', None)
            )
        except ValidationError as e:
            print(f"Error creating student: {e}")
            raise ValidationError("Error saving student profile")

        student.save()
        return user
