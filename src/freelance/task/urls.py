from django.urls import path
from task.views import *

app_name = 'task'


#this is /home/
urlpatterns = [
    path('', home_view, name='view_home'),
    path('add-problem/', add_problem, name= 'add-problem'),
    path('myapplications/', application_view, name= 'myapplications'),
    path('problems/', problem_view, name= 'problems'),
    path('problem/<int:id>/', problem_view_single, name= 'problem'),
    path('<str:user>', user_view, name = 'user')
]