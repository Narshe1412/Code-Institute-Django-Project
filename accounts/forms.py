from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import UserProfile


class UserLoginForm(forms.Form):
    """ Creates a form that allows the user to login """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
class UserRegistrationForm(UserCreationForm):
    """ Creates a form that allows the user to register an account """
    password1 = forms.CharField(widget = forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget = forms.PasswordInput, label="Password Confirmation")
    
    class Meta:
        model = User
        fields = [ 'username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        
    def clean_email(self):
        """ Cleans the email field from the form so it can be used in the DB. Checks for uniqueness as well """
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email address must be unique')
        return email
        
    def clean_password2(self):
        """ Cleans the form passwords and verify that both are the same before commiting the results to the database """
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if not password1 or not password2:
            raise forms.ValidationError("Please confirm your password")
    
        if password1 != password2:
            raise forms.ValidationError("Passwords must match")
        
        return password2
        
class UserEditForm(forms.ModelForm):
    """ Creates a form that will be used by the user when editing its django User class in the profile page """
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        
class UserProfileEditForm(forms.ModelForm):
    """ Creates a form that will be used by the user when editing its custom fields in the profile page """
    class Meta:
        model = UserProfile
        fields = ['profile', 'phone_numer']
        