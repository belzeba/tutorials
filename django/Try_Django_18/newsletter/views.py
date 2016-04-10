from django.shortcuts import render

from .forms import SignUpForm


# Create your views here.
# View for homepage
def home(request):
    # Variable for title
    title = "Welcome"

    # Add custom form to variable. If POST data is found, send it for validation, else not
    form = SignUpForm(request.POST or None)

    # Check is the user authenticated and change title if is
    if request.user.is_authenticated():
        title += " {0}".format(request.user)

    # Context variable to use with rendering
    context = {
        "title": title,
        "form": form,
    }

    # Check if given form is valid and do something if it is
    if form.is_valid():
        # Validate form and get the instance
        instance = form.save(commit=False)

        """This way we could set the name if it is missing
        full_name = form.cleaned_data.get("full_name")
        if not full_name:
            full_name = 'Anonymous'
        instance.full_name = full_name
        """
        # Save instance to database
        instance.save()

        # Edit context
        context = {
            "title": "Thank you!",
        }

    # Return the template with context
    return render(request, "base.html", context)
