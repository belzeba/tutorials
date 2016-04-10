# Default file(name) to user forms
from django import forms

from .models import SignUp


# Our custom form
class SignUpForm(forms.ModelForm):

    class Meta:
        model = SignUp
        fields = ['email']