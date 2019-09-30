from django.conf.urls import url
from .views import get_calendar

urlpatterns = [
    url(r'^$', get_calendar, name="view_events"),
    ]