from django.shortcuts import render


# Create your views here.

# View for homepage
def home(request):
    # Variable for title
    title = "World"

    # Check is the user authenticated and change title if is
    if request.user.is_authenticated():
        title = "there {0}".format(request.user)

    # Context variable to use with rendering
    context = {
        "title": title,

    }

    # Return the template with context
    return render(request, "home.html", context)
