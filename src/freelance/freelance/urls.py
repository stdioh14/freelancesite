"""freelance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from accounts.views import register_acc, login, logout
from django.urls import path, include, re_path
from task.views import *

def base_view(request):
    return render(request, 'not_found.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_acc, name= 'register'),
    path('login/', login, name= 'login'),
    path('logout/', logout, name= 'logout'),
    path('home/', include('task.urls')),
    re_path(r'^', base_view, name='back_home')
]



