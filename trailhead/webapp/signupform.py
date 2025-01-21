from django import forms
from django.contrib.auth.models import User

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    is_trip_leader = forms.BooleanField(required=False, label="Are you a trip leader?")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']