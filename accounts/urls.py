from django.urls import path
from . import views
from accounts import views


urlpatterns = [
   
    # path('register/',views.register,name = 'register'),
    path('signup/',views.signup,name ='signup'),
    # path('signin/',views.signin,name ='signin'),
    path('register/',views.register,name ='register'),
    path('login/',views.login,name ='login'),
]