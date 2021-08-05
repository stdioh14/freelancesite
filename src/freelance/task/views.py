from django.core.files.base import ContentFile
from django.core.paginator import EmptyPage, Paginator
from django.db.models import query
from django.utils import tree
from task.models import *
from django.http import HttpResponse
from django.shortcuts import render, redirect
from task.models import *
from django.contrib import messages
from .forms import CreateProblemForm
from django.db.models import Q
from django.contrib.auth.models import User




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
        problems = Problem.objects.all().filter(hidden=False)
        p = Paginator(problems, 6)

        page_num = request.GET.get('page', 1)

        try:
            page = p.page(page_num)
        except EmptyPage:
            page = p.page(1)
        
        return render(request, "home.html", {'problems': page})
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
        p = Paginator(query, 6)

        page_num = request.GET.get('page', 1)

        try:
            page = p.page(page_num)
        except EmptyPage:
            page = p.page(1)
        context = {
            'my_apps': page
        }
        return render(request, 'my_application.html', context)
    return redirect('login')


def problem_view(request):
    if(request.user.is_authenticated):
        user = request.user.username
        query = Problem.objects.all().filter(user_name__exact= user, hidden=False)
        p = Paginator(query, 6)

        page_num = request.GET.get('page', 1)

        try:
            page = p.page(page_num)
        except EmptyPage:
            page = p.page(1)
        context = {
            'problems': page
        }
        return render(request, 'problems.html', context)
    return redirect('login')

def problem_view_single(request, id):
    if(request.user.is_authenticated):

        if request.method == 'POST':
            appid = request.POST.get('appid')
            probid = request.POST.get('probid')

            Application.objects.all().filter(id=appid).update(accepted=True)
            Problem.objects.all().filter(id=probid).update(hidden=True, available=False)
            return redirect('/home/')

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

    email = User.objects.all().filter(username=user).first().email

    context = {
        'nr_entries': nr_entries,
        'nr_accepted': nr_accepted,
        'user_name': user,
        'email': email
    }

    return render(request, 'user.html', context)