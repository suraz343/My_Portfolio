from django.contrib import admin
from django.urls import path,include
from home import views



urlpatterns = [
    path('', views.index, name="index"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('verify_OTP', views.verify_OTP, name="verify_OTP"),
    path('create_password', views.create_password, name="create_password"),
    path('home', views.home, name="home"),
    path('logout',views.logoutUser, name="logout")
    
    
]
