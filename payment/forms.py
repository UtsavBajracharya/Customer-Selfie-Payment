from django import forms
from payment.models import Payment

class Form(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('payment_title', 'payment_description', 'payment_amount', 'payment_purpose')

class updateForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('payment_title', 'payment_description', 'payment_amount', 'payment_purpose')