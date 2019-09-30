from django import forms
from .models import Donation

class MakePaymentForm(forms.Form):
    """ Creates a form that will allow the user to make payments """
    MONTH_CHOICES = [(i, i) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i) for i in range(2019, 2040)]
    
    # required=False won't sent plain text to the server
    credit_card_number = forms.CharField(label='Credit Card Number', required=False)
    cvv = forms.CharField(label='Security Code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)
    
class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ('full_name', 'email', 'amount')