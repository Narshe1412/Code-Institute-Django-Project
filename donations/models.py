from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal

# Create your models here.

class Donation(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.CharField(max_length=50)
    date = models.DateField()
    amount = models.DecimalField(decimal_places=2, default=0.50, max_digits=12, validators=[MinValueValidator(Decimal('0.50'))])
    
    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)
        
    