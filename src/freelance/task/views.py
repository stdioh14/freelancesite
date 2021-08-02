from task.models import Language
import task
from django.http import HttpResponse
from django.shortcuts import render, redirect
from task.models import Language
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from .forms import CreateProblemForm



# Create your views here.
def home_view(request, *args, **kwargs):
    if(request.user.is_authenticated):
        return render(request, "home.html")
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:

            auth_login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'User or password is incorrect')
    
    context = {}
    
    return render(request, 'login.html', context)

def add_problem(request):
    form = CreateProblemForm()

    if request.method == 'POST':
        form = CreateProblemForm(request.POST or None)
        if form.is_valid():
            form.cleaned_data['user'] = request.user.username
            print(form.cleaned_data)
        
        
    
    context = {'form' : form}
    return render(request, 'add-problem.html', context)