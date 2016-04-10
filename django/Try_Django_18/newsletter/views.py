from django.shortcuts import render


# Create your views here.
# View for homepage
def home(request):
    return render(request, "home.html", {})