from django import forms 
from .models import Account


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter password',
            'class': 'form-control',
        })
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirm Password',
            'class': 'form-control',
        })
    )

   
    class Meta :
        model = Account
        fields =['firstname','lastname','phone_number','email','password']

    def __init__(self,*args,**kwargs):
        super(RegistrationForm,self).__init__(*args,**kwargs)
        self.fields['firstname'].widget.attrs['placeholder']='Enter firstname'
        self.fields['lastname'].widget.attrs['placeholder']='Enter lastname'
        self.fields['phone_number'].widget.attrs['placeholder']='Enter phone'
        self.fields['email'].widget.attrs['placeholder']='Enter email'
        self.fields['lastname'].widget.attrs['placeholder']='Enter lastname'
        for field in self.fields :
             self.fields[field].widget.attrs['class']='form-control'
