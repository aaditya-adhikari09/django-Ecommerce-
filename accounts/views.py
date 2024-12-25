from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationForm
from accounts.models import Account

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['firstname']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = Account.objects.create_user()
        
    
    context = {
        'form' : form,
    }
    return render(request ,'register.html', context)

def signup(request):
    return render(request ,'signup.html')

def logout(request):
    return render(request,'signin.html')

def account(request):
    return HttpResponse('account')