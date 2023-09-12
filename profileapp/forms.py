from .models import Profile
from django import forms
from django.forms import ModelForm
class ProfileForm(ModelForm):
    class Meta:
        model=Profile
        fields=('profile_photo',)