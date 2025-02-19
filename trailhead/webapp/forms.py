# your_app/forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Student, Subclub # Make sure Student model is imported

class BasicInfoForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    is_trip_leader = forms.BooleanField(required=False, label="Are you a trip leader?")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class PersonalDetailsForm(forms.Form):
    allergies = forms.CharField(max_length=255, required=False)
    class_year = forms.CharField(max_length=4)
    pronouns = forms.CharField(max_length=50, required=False)


class ProfilePreferencesForm(forms.Form):
    profile_picture = forms.ImageField(required=False)
    favorite_subclubs = forms.ModelMultipleChoiceField(queryset=Subclub.objects.all(), required=False)
