from django import forms
from django.shortcuts import render, redirect
from django.http import HttpResponse  
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages

from .forms import CreateUserForm

# Create your views here.

def register_acc(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('login')
            
    
    context = {'form' : form}
    return render(request, 'register.html', context)

def login(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:

            auth_login(request, user)
            return redirect('/home/')
        else:
            messages.info(request, 'User or password is incorrect')
    
    context = {}
    
    return render(request, 'login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('login')
