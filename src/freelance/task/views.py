from django.core.files.base import ContentFile
from django.db.models import query
from django.utils import tree
from task.models import *
from django.http import HttpResponse
from django.shortcuts import render, redirect
from task.models import *
from django.contrib import messages
from .forms import CreateProblemForm
from django.db.models import Q



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
            return redirect('/home/')
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
                return redirect('/home/')
    
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


def problem_view(request):
    if(request.user.is_authenticated):
        user = request.user.username
        query = Problem.objects.all().filter(user_name__exact= user)
        context = {
            'problems': query
        }
        return render(request, 'problems.html', context)
    return redirect('login')

def problem_view_single(request, id):
    if(request.user.is_authenticated):

        if request.method == 'POST':
            appid = request.POST.get('appid')
            probid = request.POST.get('probid')

            Application.objects.all().filter(id=appid).update(accepted=True)
            Problem.objects.all().filter(id=probid).update(hidden=True)




            

        user = request.user.username
        problem = Problem.objects.all().filter(id__exact = id)
        
        application = Application.objects.all().filter(problem_id__exact=id)
        context = {
            'problem': problem.first(),
            'applications': application
        }

        return render(request, 'applications.html', context)
    return redirect('login')

def user_view(request, user):
    query = Application.objects.all().filter(user_name__exact = user)
    nr_entries = query.count()
    nr_accepted = query.filter(accepted__exact=True).count()

    print("---------->" , nr_entries, nr_accepted)
    context = {
        'nr_entries': nr_entries,
        'nr_accepted': nr_accepted,
        'user': user
    }

    return render(request, 'user.html', context)