from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Military

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email")


class MilitaryForm(forms.ModelForm):
    class Meta:
        model = Military
        fields = ["rank", "first_name", "current_unit"]

class MilitaryDetailForm(forms.ModelForm):
    class Meta:
        model = Military
        fields = '__all__'