""" This was created here in tutorial for demonstration purposes only.
    There is absolutely no sense to create this in here ! """

from django.shortcuts import render


# About page
def about(request):
    context = {}
    return render(request, 'about.html', context)
