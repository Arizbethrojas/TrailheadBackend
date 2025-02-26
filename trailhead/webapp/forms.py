# your_app/forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Student 

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
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()

        # Create or update the student profile
        student = Student.objects.create(
            user=user,
            allergies=self.cleaned_data['allergies'],
            class_year=self.cleaned_data['class_year'],
            pronouns=self.cleaned_data['pronouns'],
            is_trip_leader=self.cleaned_data['is_trip_leader'],
            profile_picture=self.cleaned_data['profile_picture'],
        )
        student.save()
        return user