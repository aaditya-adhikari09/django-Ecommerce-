from django import forms 
from .models import Account

class Registrationform(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput(attrs= 
    #         'placeholder' : 'Enter password' ,   
    #         'class' : 'forms-control'))
    class Meta :
        model = Account
        fields =['firstname','lastname','phone_number','email','password']

# def __init__(self,*args,**kwargs'):
#     super(Registrationform,self).__init__(*args,**kwargs)
#         self.fields[field].widget.attrs['class']='form-control'
#     for field in self.fields :
#     self.fields[field].widget.attrs['class']='form-control'
