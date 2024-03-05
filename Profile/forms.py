from django import forms
from .models import Profile_update

class profile_update_form(forms.ModelForm):
    class Meta:
        model=Profile_update
        exclude=('user',)



