from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=30, null=False)
    solution_nr = models.IntegerField(null=False)

class Language(models.Model):
    name = models.CharField(max_length=20,unique=True, null=False)

class Problem(models.Model):
    title = models.CharField(max_length=30, null=False)
    description = models.CharField(max_length=300, null=False)
    user = models.ForeignKey(User, on_delete=CASCADE)
    language = models.ForeignKey(Language, on_delete=CASCADE)

class Application(models.Model):
    problem = models.ForeignKey(Problem, on_delete=CASCADE)
    user = models.ForeignKey(User, on_delete=CASCADE)
    