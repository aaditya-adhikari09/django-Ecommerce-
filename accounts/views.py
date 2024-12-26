from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import RegistrationForm
from accounts.models import Account
from django.contrib import messages ,auth

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
            username = email.split('@')[0]
            user = Account.objects.create_user(first_name=first_name,last_name=last_name,email = email,username = username ,password = password)
            user.phone_number = phone_number
            user.save()
            messages.success(request, 'Registration successful')
            return redirect('register')
    else :
        form = RegistrationForm()
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

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password =password)

        if user is not None :
            auth.login(request,user)
            return redirect('home')
        
        else :
            messages.error(request,'Invalid login credentials')



    return render(request ,'login.html')