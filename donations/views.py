from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from .forms import DonationForm, MakePaymentForm
from django.conf import settings
from django.utils import timezone
import stripe

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET

def checkout(request):
    if request.method == "POST":
        donation_form = DonationForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        
        if donation_form.is_valid() and payment_form.is_valid():
            donation = donation_form.save(commit=False)
            donation.date = timezone.now()
            donation.save()
            
        
            try:
                customer = stripe.Charge.create(
                    amount = int(donation.amount * 100),
                    currency = "EUR",
                    description = request.user.email if request.user.email != None else 'Anonymous Donation',
                    card = payment_form.cleaned_data['stripe_id'],
                    )
            except stripe.error.CardError:
                messages.error(request, "Your card was not authorized")
                
            if customer.paid:
                messages.error(request, "Payment successful!")
                
                return redirect(reverse('index'))
            else:
                messages.error(request, "Unable to get payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to process your card for payments")
    else:
        payment_form = MakePaymentForm()
        donation_form = DonationForm()
    return render(request, "checkout.html", {'donation_form': donation_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})
        
            
            
            
            