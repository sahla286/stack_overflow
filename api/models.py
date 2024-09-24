from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Questions(models.Model):
    title=models.CharField(max_length=100)
    question=models.CharField(max_length=1000)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    datetime=models.DateTimeField(auto_now_add=True)

class Answers(models.Model):
    answser=models.CharField(max_length=1000)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    question=models.ForeignKey(Questions,on_delete=models.CASCADE)
    datetime=models.DateTimeField(auto_now_add=True)
    upvote=models.ManyToManyField(User,related_name='upvoters')