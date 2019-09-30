from django.shortcuts import render

def index(request):
    """ Creates a basic view that will display a static page to serve as landing page """
    return render(request, "index.html")