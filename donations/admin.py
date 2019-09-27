from django.contrib import admin
from .models import Donation

# Register your models here.

class DonationInline(admin.TabularInline):
    model = Donation

admin.site.register(Donation)