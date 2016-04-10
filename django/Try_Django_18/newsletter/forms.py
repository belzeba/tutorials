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

    # Method for email validation/cleaning
    def clean_email(self):
        # Attach cleaned data
        email = self.cleaned_data.get('email')

        # Split email for more handy variables
        email_base, provider = email.split("@")
        domain, extension = provider.split(".")

        """Check if edu in email address (USA college email, I think...)
        if not extension == "edu":
            raise forms.ValidationError("Please use a valid .EDU email address")"""

        # Return the address
        return email

    # Method for name validation/cleaning
    def clean_full_name(self):
        # Attach cleaned data
        full_name = self.cleaned_data.get('full_name')

        # Own validation here

        # Return the name
        return full_name
