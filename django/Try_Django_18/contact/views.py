from django.shortcuts import render
from django.core.mail import send_mail

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
        # Get cleaned data
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")

        # Assign variables for mail
        subject = "Website Contact"
        from_email = "trydjango18@no-good.com"
        to_email = ["Taks1960@cuvox.de"]
        contact_message = "{0}: {1} via {2}".format(form_full_name, form_message, form_email)

        # Send email
        send_mail(subject,
                  contact_message,
                  from_email,
                  to_email,
                  fail_silently=False)

    # Context variable to use with rendering
    context = {
        "form": form,
    }

    # Return the template with context
    return render(request, "forms.html", context)
