from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from accounts.forms import UserLoginForm, UserRegistrationForm, UserEditForm, UserProfileEditForm
from .models import UserProfile
from donations.models import Donation

# Create your views here.
def index(request):
    return render(request, "index.html")
    
@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, "You have been logged out")
    return redirect(reverse('index'))
    

def login(request):
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
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    
    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
        
        if registration_form.is_valid():
            registration_form.save()
            
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
    donations = Donation.objects.filter(email__exact=request.user.email)
    return render(request, 'profile.html', {'userdata': request.user, 'donations': donations})
    
@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance = request.user, data=request.POST)
        profile_form = UserProfileEditForm(instance = request.user.userprofile, data=request.POST, files=request.FILES)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Profile updated successfully")
        else:
            messages.error(request, "Error updating your profile")
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = UserProfileEditForm(instance=request.user.userprofile)
    
    return render(request, 'edit_profile.html', {'user_form': user_form, 'profile_form': profile_form})
        