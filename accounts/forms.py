from django import forms 
from .models import Account

class Registrationform(forms.ModelForm):
    class Meta :
        model = Account
        fields =['firstname','lastname','phone_number','email','password']



