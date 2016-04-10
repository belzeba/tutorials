# Default file(name) to user forms
from django import forms


# Fully custom form (now basic model inheritance!)
class ContactForm(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField()
