from django.shortcuts import render


# About page
def about(request):
    context = {}
    return render(request, 'about.html', context)
