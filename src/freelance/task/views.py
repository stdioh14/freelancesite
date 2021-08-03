from task.models import *
import task
from django.http import HttpResponse
from django.shortcuts import render, redirect
from task.models import *
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from .forms import CreateProblemForm



# Create your views here.
def home_view(request, *args, **kwargs):
    if(request.user.is_authenticated):
        if request.method == 'POST':
            user = request.user.username
            problem = request.POST.get('problem')

            cnt = Application.objects.all().filter(problem_id__exact= problem).filter(user_name__exact = user).count()
            
            if cnt == 0:
                Application.objects.create(problem_id=problem, user_name = user)
                messages.warning(request, 'You successfully applied')
            else:
                messages.warning(request, 'You already applied')
            return redirect('home')
        problems = Problem.objects.all()
        return render(request, "home.html", {'problems': problems})
    return redirect('login')
    

def add_problem(request):
    if(request.user.is_authenticated):
        form = CreateProblemForm()
        user = request.user.username

        if request.method == 'POST':
            form = CreateProblemForm(request.POST or None)
            if form.is_valid():
                form.cleaned_data['user'] = user
                problem = Problem(title = form.cleaned_data['title'], description = form.cleaned_data['description'],
                                    language = form.cleaned_data['language'], user_name = form.cleaned_data['user'])
                problem.save()
                return redirect('home')
    
        context = {'form' : form}
        return render(request, 'add-problem.html', context)
    return redirect('login')


def application_view(request):
    if(request.user.is_authenticated):
        user = request.user.username
        query = Application.objects.all().filter(user_name__exact= user)
        print(query)
        context = {
            'my_apps': query
        }
        return render(request, 'my_application.html', context)
    return redirect('login')

