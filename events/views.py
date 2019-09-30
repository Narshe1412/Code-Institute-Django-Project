from django.shortcuts import render, get_object_or_404, redirect
    
def get_calendar(request):
    return render(request, "events.html")