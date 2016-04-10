from django.shortcuts import render

from .forms import ContactForm


# Create your views here.
# View for contacts
def contact(request):
    # Add custom form to variable. If POST data is found, send it for validation, else not
    form = ContactForm(request.POST or None)

    # Check if given form is valid and do something if it is
    if form.is_valid():
        """ way to print all key-value pairs ...
        for key, value in form.cleaned_data.iteritems():
            print(key, value)
        """

    # Context variable to use with rendering
    context = {
        "form": form,
    }

    # Return the template with context
    return render(request, "forms.html", context)
