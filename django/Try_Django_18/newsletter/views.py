from django.shortcuts import render

from .forms import SignUpForm


# Create your views here.
# View for homepage
def home(request):
    # Variable for title
    title = "World"

    # Check is the user authenticated and change title if is
    if request.user.is_authenticated():
        title = "there {0}".format(request.user)

    form = SignUpForm

    # Context variable to use with rendering
    context = {
        "title": title,
        "form": form,
    }

    # Return the template with context
    return render(request, "home.html", context)
