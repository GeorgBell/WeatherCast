from django import forms
from django.core import validators

class FormDetails(forms.Form):
    """
    Create forms for getting city and gender data
    """
    # City form
    city = forms.CharField(label="Your city")
    # Gender form
    CHOICES = [("M","Male"),("F","Female")]
    gender = forms.CharField(label="Your gender",
                             widget=forms.RadioSelect(choices=CHOICES))
