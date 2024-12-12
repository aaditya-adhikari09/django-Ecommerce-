from django.shortcuts import render
from django.http import HttpResponse
from .forms import Registrationform

# Create your views here.
def register(request):
    form = Registrationform()
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