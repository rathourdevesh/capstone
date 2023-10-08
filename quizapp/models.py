from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
from datetime import timedelta

# Create your models here.
class User(AbstractUser):
    pass

class Contest(models.Model):
    contestName=models.CharField(max_length=512)
    timelimit = models.IntegerField()
    maxScore = models.IntegerField()
    enrolments = models.ManyToManyField(User,related_name="enrolled",default=None,blank=True)
    subs = models.ManyToManyField(User,related_name="submitted",default=None,blank=True)
    contestTypeChoices = (("typing","typing"), ("mcq", "mcq"))
    contestType = models.CharField(max_length=20, choices=contestTypeChoices, default="mcq")

class TypingTest(models.Model):
    contestid = models.ForeignKey(Contest,on_delete=models.CASCADE)
    paragraph = models.TextField()

class Questions(models.Model):
    ansChoice = (('1','One'),('2','Two'),('3','Three'),('4','Four'),)
    contestid = models.ForeignKey(Contest,on_delete=models.CASCADE)
    question = models.CharField(max_length=2048)
    points = models.IntegerField()
    option1 = models.CharField(max_length=512)
    option2 = models.CharField(max_length=512)
    option3 = models.CharField(max_length=512)
    option4 = models.CharField(max_length=512)
    correctoption = models.CharField(max_length=5,choices=ansChoice)


class Submissions(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    contestid = models.ForeignKey(Contest,on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    subTime = models.DateTimeField(auto_now=True)
    userSubmision = models.TextField(default="")
    timeTaken = models.IntegerField(default=0)
    backspaceCount = models.IntegerField(default=0)
    totalWords = models.IntegerField(default=0)
    correctWords = models.IntegerField(default=0)
    incorrectWords = models.IntegerField(default=0)
    gwpm = models.DecimalField(decimal_places=2, max_digits=5, default=0)
    nwpm = models.DecimalField(decimal_places=2, max_digits=5, default=0)
    accuracy = models.DecimalField(decimal_places=2, max_digits=5, default=0)
    isSubmitted = models.BooleanField(default=False)
