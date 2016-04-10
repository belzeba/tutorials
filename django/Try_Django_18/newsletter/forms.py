# Default file(name) to user forms
from django import forms

from .models import SignUp


# Our custom form
class SignUpForm(forms.ModelForm):

    class Meta:
        model = SignUp
        # What fields to show in form
        fields = ['full_name', 'email']
        # exclude = ['full_name'] use sparingly
