from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
     
class UserProfile(models.Model):
    profile = models.ImageField(upload_to="profiles", default='static/img/favicon.png')
    phone_numer = PhoneNumberField(unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    