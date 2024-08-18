from django import forms
from .models import Contact_model

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact_model
        fields = ['name', 'gmail', 'phone', 'text']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['gmail'].required = True
