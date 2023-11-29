from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth import login,logout,authenticate
# Create your views here.

def register(request) : 
    form = RegisterForm()
    if request.method == 'POST' : 
        form = RegisterForm(request.POST)
        if form.is_valid() : 
            user = form.save()
            login(request , user)
            return redirect('profile')
    return render(request , 'accounts/register.html' , {'form' : form})

def profile(request) : 
    return render(request , 'accounts/dashboard.html')

def signin(request) : #login
    if request.method == 'POST' : 
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = user_name , password = password)
        # print(user)
        if user: 
            login(request , user)
            return redirect('profile')
    return render(request , 'accounts/signin.html')

def user_logout(request) : 
    logout(request)
    return redirect('signin')