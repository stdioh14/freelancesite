from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.


class Language(models.Model):
    def __str__(self) -> str:
        return self.name
    name = models.CharField(max_length=20,unique=True, null=False)
    

class Problem(models.Model):
    def __str__(self) -> str:
        return "<h3>Title:" + self.title + "</h3><h4>Description " + self.description + "</h4>" + "<h4>Posted by " + self.user_name + "</h4>" 
    title = models.CharField(max_length=30, null=False)
    description = models.CharField(max_length=300, null=False)
    user_name = models.CharField(max_length=30, null=False, default="")
    language = models.ForeignKey(Language, on_delete=CASCADE)

class Application(models.Model):
    problem = models.ForeignKey(Problem, on_delete=CASCADE)
    user_name = models.CharField(max_length=30, null=False,default="")
    accepted = models.BooleanField(default = False)

    