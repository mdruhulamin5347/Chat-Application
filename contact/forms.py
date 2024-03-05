from django import forms
from .models import Contact_model

class contact_form(forms.ModelForm):
    class Meta:
        model=Contact_model
        exclude=('user',)