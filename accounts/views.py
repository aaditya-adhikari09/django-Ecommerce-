from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def register(request):
    return render(request ,'register.html')

def signup(request):
    return render(request ,'signup.html')

def logout(request):
    return render(request,'signin.html')

def account(request):
    return HttpResponse('account')