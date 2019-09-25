from django.db import models

# Create your models here.

class Donation(models.Model):
    full_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20)
    date = models.DateField()
    amount = models.DecimalField(decimal_places=2, default=0.00, max_digits=12)
    
    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)
        
    