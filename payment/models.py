from django.db import models
from django.contrib.auth.models import User

# specifying choices 
  
PAYMENT_CHOICES = ( 
    ("Bill Payment", "Bill Payment"), 
    ("Personal Use", "Personal Use"), 
    ("Expenses", "Expenses"), 
    ("Salary", "Salary"), 
    ("Tax Payment", "Tax Payment"), 
    ("Others", "Others"), 
) 

# Create your models here.
class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    payment_title = models.CharField(max_length=100)
    payment_description = models.TextField()
    payment_purpose = models.CharField(max_length=30, choices = PAYMENT_CHOICES, default = 'Bill Payment')
    payment_time = models.DateTimeField(auto_now_add=True)
    payment_amount = models.IntegerField(default=0)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
