from django import forms
from django.db import models
from django.forms import ModelForm, fields
from .models import Problem, Language
from django import forms

class CreateProblemForm(forms.ModelForm):

    class Meta:
        model = Problem
        fields = ['title', 'description', 'language']
        
