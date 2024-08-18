from django import forms
from .models import Profile_update
from django.contrib.auth.models import User

class profile_update_form(forms.ModelForm):
    class Meta:
        model=Profile_update
        exclude=('user',)
    



class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']




