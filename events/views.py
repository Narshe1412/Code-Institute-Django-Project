from django.shortcuts import render, get_object_or_404, redirect
    
def get_calendar(request):
    """ Renders a basic google calendar in the view """
    return render(request, "events.html")