from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from accounts.forms import UserLoginForm, UserRegistrationForm, UserEditForm, UserProfileEditForm
from .models import UserProfile
from donations.models import Donation

def index(request):
    return render(request, "index.html")
    
@login_required
def logout(request):
    """ Creates a logout view that removes the user from the website """
    auth.logout(request)
    messages.success(request, "You have been logged out")
    return redirect(reverse('index'))
    

def login(request):
    """ Logs the user into the website """
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in.")
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Your username or password are incorrect")
    else :
        login_form = UserLoginForm()
    return render(request, 'login.html', {"login_form": login_form})
    
def registration(request):
    """ Registers a user into the system and records all the registration fields in the dabtase """
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    
    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
        
        if registration_form.is_valid():
            registration_form.save()
            
            ## Authenticates the user after registration
            user = auth.authenticate(username=request.POST['username'], password=request.POST['password1'])
            
            if user:
                profile = UserProfile.objects.create(user=user)
                auth.login(user=user, request=request)
                messages.success(request, "You have created your account.")
                return redirect(reverse('index'))
            else:
                messages.error(request, "There were problems creating your user.")               
            
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'registration.html', {"registration_form": registration_form})
    
    
@login_required
def view_profile(request):
    """ Creates a view with all the fields that conforms the User Profile, including donations """
    donations = Donation.objects.filter(email__exact=request.user.email)
    
    ## Fallback to avoid user errors trying to access a profile that does not exists
    if request.user.userprofile == None:
        request.user.userprofile = {'profile': None, 'phone_numer': None}
    return render(request, 'profile.html', {'userdata': request.user, 'donations': donations})
    
@login_required
def edit_profile(request):
    """ Creates a view that allows the user to edit its profile fields """
    if request.method == 'POST':
        user_form = UserEditForm(instance = request.user, data=request.POST)
        profile_form = UserProfileEditForm(instance = request.user.userprofile, data=request.POST, files=request.FILES)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Profile updated successfully")
            return view_profile(request)
        else:
            messages.error(request, "Error updating your profile")
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = UserProfileEditForm(instance=request.user.userprofile)
    
    return render(request, 'edit_profile.html', {'user_form': user_form, 'profile_form': profile_form})
        